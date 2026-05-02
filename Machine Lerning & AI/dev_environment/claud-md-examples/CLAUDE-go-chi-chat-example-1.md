# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A real-time chat application with a Go backend (HTTP + WebSocket) and a minimal web frontend. The server persists messages to SQLite and broadcasts them to connected clients over
WebSocket.

## Stack

- **Go** with [chi](https://github.com/go-chi/chi) for HTTP routing
- **SQLite3** via `github.com/mattn/go-sqlite3` (requires CGO)
- **WebSocket** via `github.com/gorilla/websocket`  
- **Frontend** — plain HTML/JS served as embedded static files (`embed.FS`)

## Commands

```bash
# Run the server
go run ./cmd/server

# Build
go build -o bin/server ./cmd/server

# Run all tests
go test ./...

# Run a single package's tests
go test ./internal/chat/...

# Run tests with race detector
go test -race ./...

# Lint
golangci-lint run
```

These commands should be run at specific points:

```bash
go test ./...          # after any change
go build -o bin/server ./cmd/server   # to verify it compiles
golangci-lint run            # before declaring work done
```

Structure

```text
cmd/
server/         # main package — wires dependencies and starts HTTP server
internal/
chat/           # core domain: Room, Client, broadcast hub
store/          # SQLite repository — message persistence
handler/        # chi HTTP + WebSocket handlers; thin, no business logic
pkg/
sqlite/         # shared DB connection setup and migration runner
```


internal/ is not importable outside this module. pkg/ is for code that could be reused across binaries (currently just DB bootstrap).

Architecture

Request flow: handler → chat (business logic) → store (persistence). Handlers must not call store directly.

The broadcast hub (internal/chat/hub.go) runs in its own goroutine. Clients register/unregister via channels — never touch the client map from outside the hub goroutine.

Migrations are plain .sql files embedded in pkg/sqlite/migrations/ and run automatically on startup in order by filename.

Environment

```text
┌─────────┬───────────┬──────────────────┐
│   Var   │  Default  │     Purpose      │
├─────────┼───────────┼──────────────────┤
│ PORT    │ 8080      │ HTTP listen port │
├─────────┼───────────┼──────────────────┤
│ DB_PATH │ ./chat.db │ SQLite file path │
└─────────┴───────────┴──────────────────┘
```


The architecture section is the most important part here — the hub's channel-based concurrency model and the handler→chat→store layering are the two things most likely to be broken
silently without explicit guidance.


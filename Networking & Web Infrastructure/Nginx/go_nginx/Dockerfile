FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY cmd/service_a/main.go .

# Build the Go application
RUN CGO_ENABLED=0 GOOS=linux go build -o service main.go

# Use a minimal alpine image for the final stage
FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/service .

# Expose the port (will be set via env var or command)
EXPOSE 3001

# Run the service
CMD ["./service"]

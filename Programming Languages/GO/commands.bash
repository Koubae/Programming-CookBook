go version

# --------------------
# Install
# --------------------

# Install other go versions
# https://go.dev/doc/manage-install
# Install
go install golang.org/dl/go1.10.7@latest
go1.10.7 download
go1.10.7 version

# Set environment
go env -w GOBIN=/somewhere/else/bin
# unset 
go env -u GOBIN


go mod init example.com/name/module
go mod init github.com/koubae/go-example

# https://github.com/golang-standards/project-layout?tab=readme-ov-file#vendor
go mod vendor

# --------------------
# Run
# --------------------
go build
go fix
go generate
go get
go install
go list
go run
go test
go vet

# compile and run 
go run . 

# Build
go build .

# Install
go install . 

go get .

# Add a dependency on the golang.org/x/example/hello/reverse package by using go get.
go get golang.org/x/example/hello/reverse
# install package
go install github.com/someuser/modname@latest

# Update module project (adds missing module requirements for imported packages and removes requirements on modules that aren't used anymore.)
go mod tidy 
go mod edit -replace example.com/greetings=../greetings

# https://go.dev/doc/modules/managing-dependencies#local_directory
go mod edit -replace=example.com/theirmodule@v0.0.0-unpublished=../theirmodule
go get example.com/theirmodule@v0.0.0-unpublished

# Download a pre-release version
# https://go.dev/doc/modules/release-workflow
go get example.com/theirmodule@v1.2.3-alpha


# remove all downloaded modules, you can pass the -modcache flag to go clean:
go clean -modcache


# "package XXX is not in GOROOT" when building a Go project
# https://stackoverflow.com/questions/61845013/package-xxx-is-not-in-goroot-when-building-a-go-project
go env -w GO111MODULE=off




# Set an installed Go module into path and run it
go install example/user/hello
export PATH=$PATH:$(dirname $(go list -f '{{.Target}}' .))
hello

# ------------------
# Builds
# ------------------
# Discover the Go install path,
go list -f '{{.Target}}'

# discover install path
go list -f '{{.Target}}'

go list -m -json -mod=readonly all

# ------------------
# Testings
# ------------------

# Run test
go test
# run test verbose
go test -v 

# fuzzing https://go.dev/doc/tutorial/fuzz
go test -fuzz=Fuzz

# ------------------
# Workspace
# ------------------
# https://go.dev/doc/tutorial/workspaces

go work init ./hello
# Add module to workspace
go work use ./example/hello
# syncs dependencies from the workspace’s build list into each of the workspace modules.
go work sync
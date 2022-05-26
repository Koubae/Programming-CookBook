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


# Update module project
go mod tidy 


# "package XXX is not in GOROOT" when building a Go project
# https://stackoverflow.com/questions/61845013/package-xxx-is-not-in-goroot-when-building-a-go-project
go env -w GO111MODULE=off


# Run test
go test
# run test verbose
go test -v 


# ------------------
# Builds
# ------------------
# Discover the Go install path,
go list -f '{{.Target}}'

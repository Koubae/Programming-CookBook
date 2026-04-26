go version
go doc fmt
# --------------------
# Install
# --------------------
# download & Install 
# ! go1.26.2 !
wget https://go.dev/dl/go1.26.2.linux-amd64.tar.gz && sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.26.2.linux-amd64.tar.gz && rm go1.26.2.linux-amd64.tar.gz


# Install other go versions
# https://go.dev/doc/manage-install
# Install
go install golang.org/dl/go1.10.7@latest
go1.10.7 download
go1.10.7 version

## Install latest version
# ref https://gist.github.com/nikhita/432436d570b89cab172dcf2894465753?permalink_comment_id=4772143#gistcomment-4772143
git clone https://github.com/udhos/update-golang
cd update-golang
sudo ./update-golang.sh

### =====================================================
## MANUAL INSTALL NEW VERSION AND INSTALL OLDER CURRENT
### =====================================================
# Alternitavelly I think we can use a much better method. First of all. 
# we also may want to keep old go available. In my case I have
# old (current): go1.24.4
# new (desired): go1.26.1
# So we can simply follow instruction from go installation doc which shows we should remove the installation
# and re-install https://go.dev/doc/install

# cheeck CPU architecture 
# If it says x86_64, use amd64. If it says aarch64, use arm64
uname -m

# 1) Remove old go and install desired go version
cd /tmp && \ 
    wget https://go.dev/dl/go1.26.1.linux-amd64.tar.gz && \ 
    sudo rm -rf /usr/local/go && \ 
    sudo tar -C /usr/local -xzf go1.26.1.linux-amd64.tar.gz && \
    rm -rf /tmp/go1.26.1.linux-amd64.tar.gz && \
    cd ~ && go version

# 2) Re-install old version 
go install golang.org/dl/go1.24.4@latest
go1.24.4 download
go1.24.4 version

# PS I assume already set path envs if not this is my current setting
# -----------------------------------------------
vim ~/.bashrc
# go
export PATH=$PATH:/usr/local/go/bin
export PATH="$HOME/go/bin:$PATH"

#export GOROOT=$HOME/go
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin

# -----------------------------------------------

### =====================================================
##  *****************************************************
### =====================================================

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
go build -o <exe-name> .

# Install
go install . 

go get .

# go get should be deprecatead and should be use with the -d flag
# https://stackoverflow.com/a/24878851/13903942 | https://stackoverflow.com/a/64800215/13903942
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


# https://pkg.go.dev/gopkg.in/yaml.v3#section-readme
go get gopkg.in/yaml.v3

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
go list -m all
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

# https://go.dev/ref/mod#environment-variables
GOWORK=off go run main.go

# Rust command-line recipes


# ---------------------------------
# Install
# ---------------------------------

# Install multiple versions
rustup toolchain install 1.85.0
rustup toolchain install 1.90.0
rustup toolchain install 1.94.0
rustup toolchain install nightly

# see what's installed 
rustup toolchain list
# current active
rustup show
# set global default
rustup default 1.94.0
rustup default stable

# local directory override
rustup override set 1.90.0
# remove override
rustup override unset

# ---------------------------------
# Build
# ---------------------------------
rustc --version
cargo build
cargo test
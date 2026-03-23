# ------------------
# General
# ------------------
# Reload without re-starting
:source ~/.vimrc
# NeoVim -- lazy io
:Lazy
:Lazy reload <plugin-name>

### Clean up neovim configs
# Linux / MacOS (unix)
rm -rf ~/.config/nvim
rm -rf ~/.local/share/nvim
rm -rf ~/.local/state/nvim
rm -rf ~/.cache/nvim

# Run neovim clean without configs
nvim --clean test.lua


# find other running Nvim instances 
pgrep -lf nvim

## Check Nvim version from Inside Nvim using Lua
:lua print("has nvim-0.12 =", vim.fn.has("nvim-0.12"))
:lua print(vim.inspect(vim.version()))
:echo exepath('nvim')

### Reinstall Nvim 
sudo apt remove -y neovim
sudo snap remove nvim 2>/dev/null || true
sudo rm -f /usr/local/bin/nvim
hash -r

# Instal Latest
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo rm -rf /opt/nvim-linux-x86_64
sudo tar -C /opt -xzf nvim-linux-x86_64.tar.gz

# Cleanup tar
rm nvim-linux-x86_64.tar.gz
# Add to Path
vim .bashrc 

export PATH="$PATH:/opt/nvim-linux-x86_64/bin"


# ------------------
# Color Schemes
# ------------------

# Shows all available colorschemes
:colorscheme <Ctrl+d>
# Press <Tab> repeatedly after typing :colorscheme — Vim will cycle through all installed colorschemes.
:colorscheme <Tab>
# Show all colors
:echo globpath(&rtp, "colors/*.vim", 0, 1)
# Cycle + preview
for f in map(split(globpath(&rtp, "colors/*.vim"), "\n"), 'fnamemodify(v:val, ":t:r")') | exe "colorscheme " . f | echo f | sleep 500m | endfor
for f in map(split(globpath(&rtp, "colors/*.vim"), "\n"), 'fnamemodify(v:val, ":t:r")') | exe "colorscheme " . f | echo f | sleep 2000m | endfor
# better!
:for f in map(split(globpath(&rtp, "colors/*.vim"), "\n"), 'fnamemodify(v:val, ":t:r")') | execute 'colorscheme ' . f | redraw | echo 'Now using: ' . f | sleep 2000m | endfor
# cycle specific themes infinitelly Ctrl-C
:while 1 | for f in ['habamax', 'evening', 'lunaperche', 'slate', 'sorbet'] | execute 'colorscheme ' . f | redraw | echo 'Now using: ' . f | sleep 2000m | endfor | endwhile



:colorscheme habamax
:colorscheme slate


# ------------------
# Editor
# ------------------
:source %           # Source current file (reload)
:e <filename>       # New file

CTRL + SPACE        # treesitter (select next node)

# Copy paste stuff...
# https://stackoverflow.com/a/39177926/13903942

`shift + drag mouse`  to select a text in vim then `ctrl + shift` + c on the terminal then `ctrl + v` on other editor



# ------------------
# Vim Plug
# ------------------
:PlugInstall to install the plugins
:PlugUpdate to install or update the plugins
:PlugDiff to review the changes from the last update
:PlugClean to remove plugins no longer in the list

# Go
:GoInstallBinaries

# ------------------
# Coc -- Language Server
# ------------------
:CocConfig

# ------------------
# Vim + NeoVim versions
# ------------------
vim --version | head -20
nvim --version
ls -la ~ | grep vim
ls -la ~/.config | grep nvim

# ------------------
# Config backups
# ------------------

# ~/.vimrc → your main Vim config
# ~/.vim/ → plugins, colorschemes, custom scripts
# ~/.viminfo → history, marks, registers
# ~/.gvimrc → GUI Vim config
# ~/.config/nvim/ → main NeoVim config
# ~/.local/share/nvim/ → plugins and installed data
# ~/.local/state/nvim/ → sessions, state, logs
# ~/.cache/nvim/ → cache files

# --------------
# Inspect current configs
ls -la ~ | grep vim
ls -la ~/.config | grep nvim
ls -la ~/.local/share | grep nvim
ls -la ~/.local/state | grep nvim
ls -la ~/.cache | grep nvim


# --------------
# backup type one
mkdir -p ~/vim-backup

[ -f ~/.vimrc ] && cp -a ~/.vimrc ~/vim-backup/
[ -d ~/.vim ] && cp -a ~/.vim ~/vim-backup/
[ -f ~/.viminfo ] && cp -a ~/.viminfo ~/vim-backup/
[ -f ~/.gvimrc ] && cp -a ~/.gvimrc ~/vim-backup/

[ -d ~/.config/nvim ] && cp -a ~/.config/nvim ~/vim-backup/
[ -d ~/.local/share/nvim ] && cp -a ~/.local/share/nvim ~/vim-backup/
[ -d ~/.local/state/nvim ] && cp -a ~/.local/state/nvim ~/vim-backup/
[ -d ~/.cache/nvim ] && cp -a ~/.cache/nvim ~/vim-backup/

[ -d ~/.config/vim ] && cp -a ~/.config/vim ~/vim-backup/
[ -f ~/.exrc ] && cp -a ~/.exrc ~/vim-backup/
[ -f ~/.ideavimrc ] && cp -a ~/.ideavimrc ~/vim-backup/
# --------------


# --------------
# Better version with timestamp
BACKUP_DIR=~/vim-backup-$(date +%Y%m%d-%H%M%S)
mkdir -p "$BACKUP_DIR"

[ -f ~/.vimrc ] && cp -a ~/.vimrc "$BACKUP_DIR/"
[ -d ~/.vim ] && cp -a ~/.vim "$BACKUP_DIR/"
[ -f ~/.viminfo ] && cp -a ~/.viminfo "$BACKUP_DIR/"
[ -f ~/.gvimrc ] && cp -a ~/.gvimrc "$BACKUP_DIR/"

[ -d ~/.config/nvim ] && cp -a ~/.config/nvim "$BACKUP_DIR/"
[ -d ~/.local/share/nvim ] && cp -a ~/.local/share/nvim "$BACKUP_DIR/"
[ -d ~/.local/state/nvim ] && cp -a ~/.local/state/nvim "$BACKUP_DIR/"
[ -d ~/.cache/nvim ] && cp -a ~/.cache/nvim "$BACKUP_DIR/"

[ -d ~/.config/vim ] && cp -a ~/.config/vim "$BACKUP_DIR/"
[ -f ~/.exrc ] && cp -a ~/.exrc "$BACKUP_DIR/"
[ -f ~/.ideavimrc ] && cp -a ~/.ideavimrc "$BACKUP_DIR/"

echo "Backup created in: $BACKUP_DIR"


# --------------
# Debug mapping
# Check what is mapping mapped to
:verbose nmap <command> 
# example
:verbose nmap gd

# runs gd (go to definition)
:lua vim.lsp.buf.definition()


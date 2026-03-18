Vim Motions
===========


* [Vim Cheat Sheet](https://vim.rtorr.com/)
* [Moving Blazingly Fast With The Core Vim Motions](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/moving-blazingly-fast-with-the-core-vim-motions/)




### Explorer

* plugins : NERDTree |  vim-vinegar 

```bash
: Ex                # enter explorer
j/k                 # move down/up
Enter or o:         # Open file/dir
-                   # Go up dir
D                   # Delete file/dir
R                   # Rename file/dir

### Creating new file / dir
%                   # Create new file name (after typed file name)
d                   # Create new dir name (after typed file name)
ctrl+L              # Same as % -- Create new file name (after typed file name)
:e <filename>       # New file

### Usefull Explorer Commands
?                   # Full list of commands
i                   # Change file display  (thin, long, wide, tree)
s                   # Sort order            (by name, time, size)
gh                  # Show hidden files
ctrl+l              # Refresh directory listing
v                   # Open file in vertical split
t                   # Open file new tab
p                   # Preview file


### File Splitting
v                   # Open file in vertical split
CTRL-w              # - Cycle Split 
CTRL-w h            # - Move to the split on the left
CTRL-w l            # - Move to the split on the right
CTRL-w j            # - Move to the split below
CTRL-w k            # - Move to the split above
CTRL-w =            # - Make all splits equal size
CTRL-w >            # - Make the current split wider
CTRL-w <            # - Make the current split narrower

## CUSTOM!!
CTRL-hjkl           # -  Go to split LEFT,DOWN,UP,RIGHT | see below Split Navigation controlls CUSTOM!!
CTRL-l              # -  Open: Vertical Split CTRL+l | see below nvim tree CUSTOM!!
CTRL-J              # -  Open: Horizontal Split CTRL+j | see below nvim tree CUSTOM!!
CTRL-B              # -  Toogle Explorer Pan | see below nvim tree CUSTOM!!
Leader+UP           # -  Split Height increase  | CUSTOM!!
Leader+DOWN         # -  Split Height decrease  | CUSTOM!!
Leader+LEFT         # -  Split Width increase  | CUSTOM!!
Leader+RIGHT        # -  Split Width decrease  | CUSTOM!!

## CUSTOM!!


CTRL-w c            # - Close current window 1 ctrl+w then quick c
CTRL-w o            # - Close all other splits, keep only current one
CTRL-w q            # - Quit current window

:Ex                 # - Return to Explorer mode in the current split



:q                  # Close current Split
:bd                 # Close bugger
:wq                 # Save and close
:x                  # Save and close (same as wq)

:source %           # Source current file (reload)
CTRL + SPACE        # treesitter (select next node)


### File Editings
u                   # Undo
CTRL+R              # Redo (r or R)
```

### NeoVim

```bash
:terminal           # open terminal
:qa                 # Close all
:qa!                # Close all (force unsaved)
:echo stdpath("config")     # Neovim config path


<space> th          # theme selector
<space> e           # open explorer

Ctrl-w h            # →  Move to the left split (usually the explorer)
Ctrl-w l            # →  Move to the right split (usually your file)
Ctrl-w w            # →  Jump to the next window


Shift   h            # Show/Hide Hidden Files


gt                   # Go to next tab
gT                   # Go to previous tab
:tabnext             # Go to next tab
:tabprev             # Go to previous tab

V                    # Select multiple lines
y                    # Copy
p                    # paste
```

```lua

# - Split Navigation controlls
vim.keymap.set("n", "<C-k>", "<C-w>k", { desc = "Go to upper split", noremap = true, silent = true })
vim.keymap.set("n", "<C-j>", "<C-w>j", { desc = "Go to lower split", noremap = true, silent = true })
vim.keymap.set("n", "<C-h>", "<C-w>h", { desc = "Go to left split", noremap = true, silent = true })
vim.keymap.set("n", "<C-l>", "<C-w>l", { desc = "Go to right split", noremap = true, silent = true })
-- Split Navigation resizing
vim.keymap.set("n", "<leader><Up>", "<C-w>+", { desc = "Increase split height", silent = true })
vim.keymap.set("n", "<leader><Down>", "<C-w>-", { desc = "Decrease split height", silent = true })
vim.keymap.set("n", "<leader><Right>", "<C-w>>", { desc = "Increase split width", silent = true })
vim.keymap.set("n", "<leader><Left>", "<C-w><", { desc = "Decrease split width", silent = true })

-- nvim tree
local function my_on_attach(bufnr)
  local api = require('nvim-tree.api')

  local function opts(desc)
    return { desc = 'nvim-tree: ' .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
  end

  -- Default mappings
  api.config.mappings.default_on_attach(bufnr)

  -- CUSTOMIZATIONS: Override split mappings
  
    -- your custom split mappings
    vim.keymap.set("n", "<C-l>", api.node.open.vertical, opts("Open: Vertical Split CTRL+l"))
    vim.keymap.set("n", "<C-j>", api.node.open.horizontal, opts("Open: Horizontal Split CTRL+j"))

end


return {
  "nvim-tree/nvim-tree.lua",
  version = "*",
  lazy = false,
  dependencies = {
    "nvim-tree/nvim-web-devicons",
  },
  config = function()
     local nvimtree = require("nvim-tree")

     vim.g.loaded_netrw = 1
     vim.g.loaded_netrwPlugin = 1

    require("nvim-tree").setup {
        on_attach = my_on_attach
    }

    vim.keymap.set("n", "<c-b>", ":NvimTreeFindFileToggle<CR>")


  end,
}

```

### Shortcuts for neovim -- golang quickstart setup 


**Your leader key here is Space.**

```bash
<leader>ff   find files
<leader>fg   grep in project
<leader>fb   buffers
gd           go to definition
gr           references
gI           implementations
K            hover docs
<leader>rn   rename symbol
<leader>ca   code action
<leader>f    format file
<leader>w    save
<leader>q    quit

```




### keybindings Vim Options meaning

Example

```bash
vim.keymap.set("n", "<leader>e", ":Ex<CR>")

``` 

* vim.keymap.set(...) → create a key mapping
* "n" → only in normal mode
* "<leader>e" → press Space, then e
* ":Ex<CR>" → run the Vim command :Ex and press Enter automatically
* <CR> means Carriage Return, basically the Enter key. (presses Enter automatically)

##### Small cheat sheet of useful key notation

* <leader> = your leader key, here Space
* <localleader> = secondary leader key
* <CR> = Enter
* <Esc> = Escape
* <Tab> = Tab
* <S-Tab> = Shift+Tab
* <C-x> = Ctrl+x
* <A-x> = Alt+x
* <M-x> = Meta/Alt+x
* <BS> = Backspace

Examples:

* <C-h> → Ctrl+h
* <C-s> → Ctrl+s
* <leader>e → Space e


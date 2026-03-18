NeoVim
======


# **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**
## **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**
### **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**
### **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**
#### **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**
#### **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**

* **Check also my NeoVim configuration setup [Koubae/nvim](https://github.com/Koubae/nvim)**


* [The Only Video You Need to Get Started with Neovim](https://www.youtube.com/watch?v=m8C0Cq9Uv9o)
    * [nvim-lua/kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim)
* [How I Setup Neovim To Make It AMAZING in 2024: The Ultimate Guide](https://www.youtube.com/watch?v=6pAG3BHurdM)
    * [josean-dev/dev-environment-files](https://github.com/josean-dev/dev-environment-files/tree/main)
    * [VS Code josean-dev/dev-environment-files](https://github.com/auth/github_editor?redirect=%2Fjosean-dev%2Fdev-environment-files%2Fblob%2Fmain%2F.config%2Fnvim%2Flua%2Fjosean%2Fplugins%2Finit.lua&requestId=37c20ea5-fdb2-4ebe-9d5e-93652dc34e4b)

* [The perfect Neovim setup for Go (Nvchad) ](https://www.youtube.com/watch?v=i04sSQjd-qo)
    * [dreamsofcode-io/neovim-go-config](https://github.com/dreamsofcode-io/neovim-go-config)
* [(setup with Lazy) My Neovim configuration for Golang development in 2024 (Using lazy.nvim and go.nvim)](https://www.youtube.com/watch?v=n5_WLgxwkU8)
* [Configure Golang in Neovim](https://www.youtube.com/watch?v=EgwiPok2nbU)
    * [exosyphon/nvim](https://github.com/exosyphon/nvim)


* [Teaching Neovim From Scratch To A Noob](https://www.youtube.com/watch?v=-ybCiHPWKNA)

### CheckList

That's all the crap you need to learn and setup for Neovim but is freaking worth it!

* Install Neovim - possibly more stuff
* Setup Neovim config file structure
* Generic settings (similar to Vim `.vimrc`)
* Keymaps -- Generics
* Plugin manager -- Lazy -- or -- NvChad --
* Navigator -- vim-tmux-navigator
* theme -- colorscheme
* File explorer
* which-key (shows all keymaps for a keyboard key)
* fuzzy finder
* greeter
* auto sessions (save/reload sessions)
* bufferline
* statusline
* dressing.nvim (general UI improving)
* maximize splits
* treesitter
* indent guides
* autocomplete
* autopairs
* todo comments
* substitution
* nvim-surround
* lsp 
* formatting
* linting
* git integration


### Plugin Manager

* [Nvchad vs lazyvim](https://www.reddit.com/r/neovim/comments/1b0llw7/nvchad_vs_lazyvim/)

### Install

**WSL**

```bash
#wsl --install
#wsl
sudo add-apt-repository ppa:neovim-ppa/unstable -y
sudo apt update
sudo apt install make gcc ripgrep unzip git xclip fd-find neovim 
```


### Quickstart


Fresh start

Neovim + lazy.nvim, then: add only six things
* LSP
* completion
* treesitter
* formatter
* fuzzy finder
* small statusline


```bash
# Verifiy this works
nvim --version
go version
git --version
rg --version

# the install go tools

go install golang.org/x/tools/gopls@latest
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/go-delve/delve/cmd/dlv@latest

# 2. Put this in your config
mkdir -p ~/.config/nvim
nvim ~/.config/nvim/init.lua

# for tree sitter thingy
npm install -g tree-sitter-cli
```


Paste this entire file:


```lua
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Basic editor settings
local opt = vim.opt
opt.number = true
opt.relativenumber = true
opt.mouse = "a"
opt.ignorecase = true
opt.smartcase = true
opt.termguicolors = true
opt.signcolumn = "yes"
opt.updatetime = 250
opt.timeoutlen = 300
opt.splitright = true
opt.splitbelow = true
opt.scrolloff = 8
opt.sidescrolloff = 8
opt.tabstop = 4
opt.shiftwidth = 4
opt.softtabstop = 4
opt.expandtab = false

-- Quick save / quit
vim.keymap.set("n", "<leader>w", "<cmd>w<cr>", { desc = "Write" })
vim.keymap.set("n", "<leader>q", "<cmd>q<cr>", { desc = "Quit" })
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Line diagnostics" })

-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
local uv = vim.uv or vim.loop
if not uv.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  -- Treesitter
  {
    "nvim-treesitter/nvim-treesitter",
    branch = 'master',
    build = ":TSUpdate",
    lazy = false,
    main = "nvim-treesitter.configs",
    opts = {
      ensure_installed = {
        "go",
        "gomod",
        "gowork",
        "gosum",
        "lua",
        "vim",
        "vimdoc",
        "bash",
        "json",
        "yaml",
        "markdown",
        "markdown_inline",
      },
      auto_install = true,
      highlight = { enable = true },
      indent = { enable = true },
    },
  },

  -- Telescope
  {
    "nvim-telescope/telescope.nvim",
    version = "*",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local builtin = require("telescope.builtin")
      vim.keymap.set("n", "<leader>ff", builtin.find_files, { desc = "Find files" })
      vim.keymap.set("n", "<leader>fg", builtin.live_grep, { desc = "Live grep" })
      vim.keymap.set("n", "<leader>fb", builtin.buffers, { desc = "Buffers" })
      vim.keymap.set("n", "<leader>fh", builtin.help_tags, { desc = "Help tags" })
    end,
  },

  -- Completion
  {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "L3MON4D3/LuaSnip",
    },
    config = function()
      local cmp = require("cmp")
      cmp.setup({
        snippet = {
          expand = function(args)
            require("luasnip").lsp_expand(args.body)
          end,
        },
        mapping = cmp.mapping.preset.insert({
          ["<C-Space>"] = cmp.mapping.complete(),
          ["<C-n>"] = cmp.mapping.select_next_item(),
          ["<C-p>"] = cmp.mapping.select_prev_item(),
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
        }),
        sources = {
          { name = "nvim_lsp" },
        },
      })
    end,
  },

  -- Formatting
  {
    "stevearc/conform.nvim",
    event = { "BufWritePre" },
    opts = {
      formatters_by_ft = {
        go = { "goimports", "gofmt" },
      },
      format_on_save = {
        timeout_ms = 500,
        lsp_fallback = true,
      },
    },
  },

  -- LSP
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
    },
    config = function()
      local capabilities = require("cmp_nvim_lsp").default_capabilities()

      vim.api.nvim_create_autocmd("LspAttach", {
        callback = function(event)
          local builtin = require("telescope.builtin")

          local map = function(keys, func, desc)
            vim.keymap.set("n", keys, func, {
              buffer = event.buf,
              desc = desc,
            })
          end

          map("gd", builtin.lsp_definitions, "Go to definition")
          map("gr", builtin.lsp_references, "References")
          map("gI", builtin.lsp_implementations, "Implementations")
          map("K", vim.lsp.buf.hover, "Hover")
          map("<leader>rn", vim.lsp.buf.rename, "Rename")
          map("<leader>ca", vim.lsp.buf.code_action, "Code action")
          map("<leader>f", function()
            require("conform").format({ async = true, lsp_fallback = true })
          end, "Format buffer")
        end,
      })

      vim.lsp.config("gopls", {
        capabilities = capabilities,
        settings = {
          gopls = {
            gofumpt = true,
            staticcheck = true,
            completeUnimported = true,
            usePlaceholders = true,
            analyses = {
              unusedparams = true,
              shadow = true,
            },
          },
        },
      })

      vim.lsp.enable("gopls")
    end,
  },

  -- Statusline
  {
    "nvim-lualine/lualine.nvim",
    opts = {
      options = {
        theme = "auto",
      },
    },
  },
}, {
  change_detection = { notify = false },
    rocks = {
    enabled = false,
  },

  pkg = {
    sources = {
      "lazy",
      "packspec",
    },
  },

})

```

next


```bashs
# launch neovim
nvim
# then run:
:checkhealth
:checkhealth vim.lsp
:checkhealth telescope

```


**shortcuts**


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



### Videos

* [AstroNvim Tutorial 2025: Complete Setup Guide for Neovim Beginners (Mastering Neovim Part 2)](https://www.youtube.com/watch?v=S83XpVALvtU)
* [0 to LSP : Neovim RC From Scratch -- The Primeagen](https://www.youtube.com/watch?v=w7i4amO_zaE)
* [What’s the BEST Neovim Distro? (LazyVim vs AstroNvim vs NvChad + more)](https://www.youtube.com/watch?v=Z1qEKUf0ibk)


* Playlist: [astrovim + go](https://www.youtube.com/playlist?list=PL9IfXylCrZ1jd3FRLk_-oS5nZQpaOiYAf)

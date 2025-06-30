Vim Family
==========

Vim-like IDE includes:

* [Vi](https://en.wikipedia.org/wiki/Vi_(text_editor))
* [Vim](https://www.vim.org/)
* [NeoVim](https://neovim.io/)
* [Emacs](https://www.gnu.org/software/emacs/)
* [Nano](https://www.nano-editor.org/)



Vim
------

* [Awesome Vim Color Schemes](https://github.com/rafi/awesome-vim-colorschemes)
* [What’s your favorite dark colorscheme](https://www.reddit.com/r/vim/comments/g3b8su/whats_your_favorite_dark_colorscheme/)
* [gruvbox](https://github.com/morhetz/gruvbox)
* [badwolf](https://github.com/sjl/badwolf)
* [Neovim + Item2 + Truecolor = Awesome](https://medium.com/@ericclifford/neovim-item2-truecolor-awesome-70b975516849)

* [VimCharm: Approximating PyCharm on vim](https://kevinmartinjose.com/2020/11/22/vimcharm-approximating-pycharm-on-vim/)
* [JetBrains-Inspired colorscheme for Vim](https://www.reddit.com/r/vim/comments/17lf643/jetbrainsinspired_colorscheme_for_vim/)
* [VimCharm](https://github.com/kevinmartinjos/vimcharm)

### Tutorials

* [Youtube -- ThePrimeagen Vim As Your Editor - Introduction](https://www.youtube.com/watch?v=X6AR2RMB5tE&list=PLm323Lc7iSW_wuxqmKx_xxNtJC_hJbQ7R)

* [Vim Adventures](https://vim-adventures.com/)
* [openvim](https://openvim.com/)
* [VIM and Python – A Match Made in Heaven](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
* [How to Install a Theme in VIM (Without a Plugin Manager)](https://www.youtube.com/watch?v=HmSJ2BxDvwU)

### vimrc examples

* [kevinmartinjos/vimcharm/](https://github.com/kevinmartinjos/vimcharm/blob/master/.vimrc)

### Package Managers


* [junegunn/vim-plug](https://github.com/junegunn/vim-plug)
* [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen)


### Language Server

* [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)


**See below instructions [Coc Setup](#coc-setup)** 

### VIM Bundles

* [fatih/vim-go](https://github.com/fatih/vim-go)


### GO

* [nosarthur .vim/coc-settings.json](https://github.com/nosarthur/dotfiles/blob/main/.vim/coc-settings.json)
* [nosarthur /dotfiles/blob/main/.vimrc](https://github.com/nosarthur/dotfiles/blob/main/.vimrc)

NeoVim
------

### Tutorials

* [Youtube -- teej_dv](https://www.youtube.com/@teej_dv)



More Videos
-----------


* [Youtube -- Vim vs NeoVim, What's the Difference? Which Should You Use?](https://www.youtube.com/watch?v=R8tI4gpzkE4)
* [Youtube -- ThePrimeagen explains Neovim to Lex Fridman](https://www.youtube.com/watch?v=PkbjvbjLAug)
* [Youtube -- How to Do 90% of What Plugins Do (With Just Vim)](https://www.youtube.com/watch?v=XA2WjJbmmoM)


Further Reading
---------------

* [Vim vs. NeoVim?](https://www.reddit.com/r/vim/comments/pzo6tg/vim_vs_neovim/)
* [Should I use vim or neovim?](https://www.reddit.com/r/vim/comments/opvv66/should_i_use_vim_or_neovim/)
* [Why I Stopped Using Vim After 2 Years Of Using It](https://www.youtube.com/watch?v=JZMcjGxJ8Qw&t=32s)
* [Vim Tutorial for Beginners](https://www.youtube.com/watch?v=RZ4p-saaQkc)



### Coc Setup + GO

* [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)
* [Vim setup for go programmers: conquer of completion (coc) and vim-go](https://www.youtube.com/watch?v=nfJlc-OpsJE)

* [nosarthur .vim/coc-settings.json](https://github.com/nosarthur/dotfiles/blob/main/.vim/coc-settings.json)
* [nosarthur /dotfiles/blob/main/.vimrc](https://github.com/nosarthur/dotfiles/blob/main/.vimrc)

```bash
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
go install golang.org/x/tools/gopls@latest

# vim .bashrc
# Add
export PATH=$PATH:/usr/local/go/bin
export PATH="$HOME/go/bin:$PATH"
```

```json
{
  "python.linting.flake8Args": [
    "--ignore=E123,E125,E126,E127,E128,E201,E221,E252,E265,E303,E501,W391"
  ],
  "python.linting.flake8Enabled": true,
  "python.linting.pydocstyleEnabled": true,
  "python.analysis.useLibraryCodeForTypes": false,
  "python.jediEnabled": false,
  "suggest.noselect": true,
  "coc.preferences.formatOnSaveFiletypes": ["css", "markdown", "json"],
  "languageserver": {
    "golang": {
      "command": "gopls",
      "rootPatterns": ["go.mod", ".vim/", ".git/", ".hg/"],
      "filetypes": ["go"],
      "initializationOptions": {
        "usePlaceholders": true
      }
    }
  }
}
```

Varian 2 for GO

```json
{
  "languageserver": {
    "golang": {
      "command": "gopls",
      "rootPatterns": ["go.mod", ".git/", ".hg/"],
      "filetypes": ["go"],
      "initializationOptions": {
        "usePlaceholders": true,
        "completeUnimported": true,
        "staticcheck": true
      }
    }
  },

  "suggest.noselect": false,
  "suggest.enablePreview": true,
  "diagnostic.enable": true,
  "diagnostic.checkCurrentLine": true,
  "diagnostic.virtualText": true,
  "diagnostic.displayByAle": false,

  "go.formatTool": "goimports",
  "go.lintTool": "golangci-lint",
  "go.lintOnSave": true,
  "go.buildOnSave": false,
  "go.vetOnSave": true
}
```
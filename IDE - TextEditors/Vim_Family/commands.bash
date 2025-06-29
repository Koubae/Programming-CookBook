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
rm -rf ~/.local/state/nvim
rm -rf ~/.local/share/nvim

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
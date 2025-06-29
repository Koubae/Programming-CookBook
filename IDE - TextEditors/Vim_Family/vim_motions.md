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
:Ex                 # - Return to Explorer mode in the current split

:q                  # Close current Split
:bd                 # Close bugger
:wq                 # Save and close
:x                  # Save and close (same as wq)

:source %           # Source current file (reload)
CTRL + SPACE        # treesitter (select next node)
```
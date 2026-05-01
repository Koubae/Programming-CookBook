# Start Claude Code
claude
# claude location
~/.local/bin/claude


# Then login using Console / platform billing
claude auth login --console
# Check login
claude auth status


# one time task 
claude "sum 1 + 1"
# one time task & exit
claude -p "sum 1 + 1"
# continue most recent convo in current dir
claude -c
# resume prev convo 
claude -r
# erase convo history
/clear
# show ava commands 
/help

### Cool commands

# Bulk operations across files
git diff main --name-only | claude -p "review these changed files for security issues"

# claude location
~/.local/bin/claude
# Start Claude Code
claude
# start claude plan mdoe
claude --permission-mode plan
claude --permission-mode plan -p "Plan message..."

# Then login using Console / platform billing
claude auth login --console
# Check login
claude auth status

# restart sessions where was left-off
claude --continue
claude --resume
# session To branch off and try a different approach without affecting the original session, use the --fork-session flag:
claude --continue --fork-session


# one time task 
claude "sum 1 + 1"
# one time task & exit
claude -p "sum 1 + 1"
# continue most recent convo in current dir
claude -c
# resume prev convo 
claude -r
# erase convo history | creates new sesions
/clear
# show ava commands 
/help
# walks you through creating a CLAUDE.md for your project
/init 
# diagnoses common issues with your installation
/doctor 

# is a picker shows sessions from the current worktree by default, with keyboard shortcuts to widen the list to other worktrees or projects
# https://code.claude.com/docs/en/common-workflows#resume-previous-conversations
/resume

# see what’s using context window space
# https://code.claude.com/docs/en/how-claude-code-works#the-context-window
/context

# rules / context compactation
/compact
/compact <msg>



### Cool commands

# Bulk operations across files
git diff main --name-only | claude -p "review these changed files for security issues"



#### Work Trees
# https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees
# Start Claude in a worktree named "feature-auth"
# Creates .claude/worktrees/feature-auth/ with a new branch
claude --worktree feature-auth

# Start another session in a separate worktree
claude --worktree bugfix-123


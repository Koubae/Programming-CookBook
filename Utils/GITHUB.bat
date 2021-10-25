# ========================= < COLLECTION OF GITHUB COMMANDS > ========================= #


# ------------------------------ < BRANCH > ------------------------------ #

# Create Branch 
git branch <branch-name>
# Switch Branch
git checkout <branch-name>
# Create and Swith Branch
git checkout -b <branch-name>


# ------------------------------ < CONFIGS > ------------------------------ #
# 1. System level (applied to every user on the system and all their repositories)

# to view (may need sudo)
git config --list --system 
# to set, 
git config --system color.ui true
# to edit system config file
git config --edit --system


#2. Global level (values specific personally to you, the user. )
# to view
git config --list --global
# to set
git config --global user.name xyz
# to edit global config file
git config --edit --global


#3. Repository level (specific to that single repository)
# View
git config --list --local
# Set
git config --local core.ignorecase true (--local optional)
# Edit Config FIle
git config --edit --local (--local optional)

# View all settings
git config --list, showing system, global, and (if inside a repository) local configs
git config --list --show-origin, also shows the origin file of each config item

# Read one particular confi
git config user.name to get user.name, for example.
# options 
--system, --global, --local #  to read that value at a particular level.

# ---------- Setting User & Email for repos

git config user.name "Your Name Here"
git config user.email your@email.com

# For (global) default email (which is configured in your ~/.gitconfig):

git config --global user.name "Your Name Here"
git config --global user.email your@email.com



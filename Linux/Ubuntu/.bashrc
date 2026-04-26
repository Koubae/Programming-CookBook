# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    #PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;35m\]\W\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias lf='ls -CF'
alias l='ls -1 --group-directories-first'
# https://stackoverflow.com/questions/66832570/how-to-check-allocated-memory-for-wsl-docker
# check free mem 
alias f="free -mh"

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

#### CUSTOM


if [ -f ~/.bash_colors ]; then
       . ~/.bash_colors
fi


# Adds color to branch!
# https://medium.com/@chiraggandhi70726/how-to-add-git-branch-name-to-bash-prompt-b112b93606e#:~:text=In%20order%20to%20add%20a,bash_profile).
parse_git_branch() {
    #  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
    git rev-parse --abbrev-ref HEAD
}

__git_ps1_custom() {
    __git_ps1 "\001${On_Green}\002\001${BIGreen}\002(%s)\001${Color_Off}\002 "
}



export PS1="\$(__git_ps1_custom)${PS1}"



#### PATH

export PATH="/usr/local/bin/:$PATH"

# pyenv
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"

# pipenv
export PATH="$HOME/.local/bin:$PATH"

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:
eval "$(pyenv virtualenv-init -)"

# go
export PATH=$PATH:/usr/local/go/bin
export PATH="$HOME/go/bin:$PATH"

#export GOROOT=$HOME/go
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin

# nvm, npm, node
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


### JAVA
export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
export PATH="$JAVA_HOME/bin:$PATH"

use_java8() {
  export JAVA_HOME=/home/fb/.jdks/corretto-1.8.0_472
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java17() {
  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java21() {
  export JAVA_HOME=/usr/lib/jvm/java-21-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java24() {
  export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

export PATH="/opt/gradle/current/bin:$PATH"


#### Alias

function create_python_env() {
    if [ -d .venv ]; then
        echo ".venv directory exists";
    else
        echo ".venv does not exists -- creating ...";
        echo PIPENV_VENV_IN_PROJECT=1 >> .env;pipenv install --python=$(which python);
    fi
}

alias PYTHON_ENV=create_python_env



# AWS
# https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-completion.html

complete -C '/usr/local/bin/aws_completer' aws


export PATH="$HOME/ijhttp:$PATH"

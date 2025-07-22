.bashrc Templates
=================


### .bashrc setup

```bash


function create_python_env() {
    if [ -d .venv ]; then
        echo ".venv directory exists";
    else
        echo ".venv does not exists -- creating ...";
        echo PIPENV_VENV_IN_PROJECT=1 >> .env;pipenv install --python=$(which python);
    fi
}

alias PYTHON_ENV=create_python_env


```

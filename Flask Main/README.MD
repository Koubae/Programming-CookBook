# Flask -Main
=======================






-----------------------------------------------------------------------------------------------------

## Features

- [Custom Commands](https://flask.palletsprojects.com/en/1.1.x/cli/#custom-commands)
- [Click](https://click.palletsprojects.com/en/7.x/)
- [Testing CLI Commands](https://flask.palletsprojects.com/en/1.1.x/testing/#testing-cli)
- [Testing Click Applications](https://click.palletsprojects.com/en/7.x/testing/)


```

from flask import Flask

app = Flask(__name__)

@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    ...

```

```
$ flask create-user admin
```

This example adds the same command, but as user create, a command in a group. This is useful if you want to organize multiple related commands.

```

from flask import Flask
from flask.cli import AppGroup

app = Flask(__name__)
user_cli = AppGroup('user')

@user_cli.command('create')
@click.argument('name')
def create_user(name):
    ...

app.cli.add_command(user_cli)

```

```
$ flask user create demo
```


### 


-----------------------------------------------------------------------------------------------------

Nginx
=====

Change `NGINX_CONF_PATH` env variable in [.env.nginx](./.env.nginx) file to point to your custom nginx configuration file.

QuickStart
----------

Start Nginx:
```bash
make nginx-up
```

### Makefile Commands

- `make nginx-up` - Start Nginx container in detached mode
- `make nginx-down` - Stop and remove Nginx container
- `make nginx-terminal` - Connect to Nginx CLI terminal
- `make help` - Show available commands

### Usage

Start Nginx:
```bash
make nginx-up
```

Connect to Nginx CLI:
```bash
make nginx-terminal
```

Stop Nginx:
```bash
make nginx-down
```

Guide / Notes
-------------

* /usr/share/nginx/html is the standard/default path for static HTML files in the official nginx Docker image.
* the official nginx Docker image, the default "Welcome to nginx!" page lives at /usr/share/nginx/html/index.html

#### Check default configs

```bash
docker exec nginx ls /etc/nginx/conf.d/
docker exec nginx cat /etc/nginx/conf.d/default.conf
```




# jump into nginx container
docker exec -it nginx bash
# or use makefile
make nginx-terminal

# tests the nginx configuration file for syntax errors.
nginx -t 


# reload nginx configuration
nginx -s reload
# -s stands for "signal" - it sends a signal to the nginx master process.
# reload - gracefully reload configuration
nginx -s reload
# stop - shut down quickly
nginx -s stop
# quit - shut down gracefully
nginx -s quit
# reopen - reopen log files
nginx -s reopen


# -------------------------
# Configs
# -------------------------
nginx -T

# -------------------------
# Logs
# -------------------------
docker exec nginx tail -10 /var/log/nginx/access.log
nginx tail -10 /var/log/nginx/access.log

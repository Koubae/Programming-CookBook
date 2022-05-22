#  generate a self-signed SSL certificate using OpenSSL?
# Credit: https://stackoverflow.com/a/10176685/13903942
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

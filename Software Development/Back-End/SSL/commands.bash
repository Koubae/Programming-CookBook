#  generate a self-signed SSL certificate using OpenSSL?
# Credit: https://stackoverflow.com/a/10176685/13903942
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365


# credit https://stackoverflow.com/a/41366949/13903942
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
  -keyout example.key -out example.crt -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:www.example.net,IP:10.0.0.1"
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === '906a84df04cea2aa72f40b5f787e49f22d4c2f19492ac310e8cba5b96ac8b64115ac402c8cd292b8a03482574915d1a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"


# Install Packages

composer install 

# C:\wamp\bin
# C:\wamp\bin\php
# Create a file (use notepad) composer.bat in the same folder and add this line to it:

@php C:\wamp\bin\php\php5.4.12\composer.phar %*
# Close and try to run composer from anywhere:

cd\
composer --version
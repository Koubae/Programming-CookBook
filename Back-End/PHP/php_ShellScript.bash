# ===========================================
#       MISC
# ===========================================

# Run build-in server
php -S localhost:8000
# Starting with a specific document root directory
php -S localhost:8080 -t public/
# ------------------ Show Apache logs in terminal 
# install UnxUtils  https://sourceforge.net/projects/unxutils/
# install BareTail  # install UnxUtils  https://sourceforge.net/projects/unxutils/
# Linux
tail -f your_log_file
# Windows
Get-Content path_of_file_log -Wait -Tail 30

# ------- Type checking
# Check error in project
composer require --dev squizlabs/php_codesniffer
composer require --dev peridot-php/peridot
composer require --dev peridot-php/leo
composer require --dev eloquent/phony-peridot

# check if any code syntax is wrong
./vendor/bin/phpcs — standard=psr2 App/
# in case you have only white-spaces errors
./vendor/bin/phpcbf — standard=psr2 App/
# ----------------

# ===========================================
#       COMPOSER
# ===========================================
# Start composert and create composer.json
composer init 
# add package to composer.json + add package to ./vendor
composer require [package_name]

# Update autoload this below has to be added to composer.json
# "autoload": {
#   "psr-4": {
#     "App\\": "App/"
#    }
# },
composer dump-autoload

# Run composer scripts
# "scripts": {
#    "test": ["./vendor/bin/phpcs --standard=psr2 App/"]
# },
composer run-script test
# even shorter with 
composer test

# ===========================================
#       LARAVEL
# ===========================================
# Global install with Composer
composer global require laravel/installer 

# Create a new Laravel Project 
laravel new [projectname]

# create a new Laravel application in a directory , you may run the following command in your terminal:
curl -s https://laravel.build/[project_NAME] | bash
cd [project_NAME]
./vendor/bin/sail up


# Sail Services: Available services include mysql, pgsql, mariadb, redis, memcached, meilisearch, minio, selenium, and mailhog:
# mysql, redis, meilisearch, mailhog, and selenium
curl -s "https://laravel.build/example-app?with=mysql,redis" | bash


# ===========================================
#       ARTISAN
# ===========================================
php artisan

# Run PHP Server
php artisan serve

# Auth
php artisan make:auth

# To enable maintenance mode, execute the down Artisan command:
php artisan down
# efresh HTTP header to be sent with all maintenance mode
php artisan down --refresh=15
# provide a retry option to the down command, which will be set as the Retry-After HTTP header's value, although browsers generally ignore this header
php artisan down --retry=60
# Even while in maintenance mode, you may use the secret option to specify a maintenance mode bypass token:
php artisan down --secret="1630542a-246b-4b66-afa1-dd72a4c43515"
# After placing the application in maintenance mode, you may navigate to the application 
# URL matching this token and Laravel will issue a maintenance mode bypass cookie to your browser:

# https://example.com/1630542a-246b-4b66-afa1-dd72a4c43515

#pre-render


php artisan down --render="errors::503"
#  instruct Laravel to redirect all requests to a specific URL. 
# This may be accomplished using the redirect option. For example, you may wish to redirect all requests to the / URI:
php artisan down --redirect=/
#To disable maintenance mode
php artisan up

# review the available commands of Class build (make)
php artisan list make

# ----------------- Eloquent

php artisan make:model [ModelName]

# Make Model , Factory, Migration, Seeder, Reqyestm Controller, Policy
php artisane make:model [ModelName] --all

# Create Model , DB Migrations , Controller
php artisan make:model [ModelName] -mc

# ----------------- Route
# Lists all Route
php artisan route:list

# ----------------- Controller
php artisan make controller [controllerName]


# ----------------- Database
# connect to db
php artisan db
php artisan db mysql


# Make Laravel Migration 
php artisan make:migration [table_name]

# Migrate Laravel MIgration 
php artisan migrate

# Add a new column to existing table
# More on StackOverflow --> https://stackoverflow.com/a/16791988/13903942
php artisan make:migration add_[column_name]_to_[table_name]_table --table=[table_name]


# ----------------- Components
php artisan make:component Alert
# Will create an Input component in the App\View\Components\Forms directory 
# and the view will be placed in the resources/views/components/forms directory.
php artisan make:component Forms/Input


# ===========================================
#       SAIL
# ===========================================
./vendor/bin/sail up
./vendor/bin/sail php --version
# Instead of repeatedly typing vendor/bin/sail to execute Sail commands, 
# you may wish to configure a Bash alias that allows you to execute Sail's commands more easily

alias sail='[ -f sail ] && bash sail || bash vendor/bin/sail'
# start all of the Docker containers in the background, you may start Sail in "detached" mode
sail up -d

# Stop all containers
sail stop

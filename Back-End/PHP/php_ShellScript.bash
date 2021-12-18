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

# Make Laravel Migration 
php artisan make:migration [table_name]

# Migrate Laravel MIgration 
php artisan migrate

# Add a new column to existing table
# More on StackOverflow --> https://stackoverflow.com/a/16791988/13903942
php artisan make:migration add_[column_name]_to_[table_name]_table --table=[table_name]


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

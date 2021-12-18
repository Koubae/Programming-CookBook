Laravel
=======================

If getting error about a port change the `docker-Compose.yml` with
```docker
ports:
- "8084:80"
``` 

### Installations 

If your computer already has PHP and Composer installed, you may create a new Laravel project by using Composer directly. After the application has been created, you may start Laravel's local development server using the Artisan CLI's serve command

```bash
composer create-project laravel/laravel example-app
cd example-app
php artisan serve
```

** Laravel Installer as a global Composer dependency**
composer global require laravel/installer

Make sure to place Composer's system-wide vendor bin directory in your $PATH so the laravel executable can be located by your system. This directory exists in different locations based on your operating system; however, some common locations include:

* macOS: `$HOME/.composer/vendor/bin`
* Windows: `%USERPROFILE%\AppData\Roaming\Composer\vendor\bin`
* GNU / Linux Distributions: `$HOME/.config/composer/vendor/bin` or ``$HOME/.composer/vendor/bin``

```bash
laravel new example-app
cd example-app
php artisan serve
```
* To indicate that you want a Git repository to be created
```bash
laravel new example-app --git
cd example-app
php artisan serve
```

Main Components
-------------------------

* [Laravel Sail](https://laravel.com/docs/8.x/sail)
* [Service Container](https://laravel.com/docs/8.x/container)
* [Testing](https://laravel.com/docs/8.x/testing)
* [Queues](https://laravel.com/docs/8.x/queues)
* [Broadcasting](https://laravel.com/docs/8.x/queues)
* [Laravel Vapor](https://vapor.laravel.com)

#### Laravel Basics

* [Request Lifecycle](https://laravel.com/docs/8.x/lifecycle)
* [Configuration](https://laravel.com/docs/8.x/configuration)
* [Directory Structure](https://laravel.com/docs/8.x/structure)
* [Service Container](https://laravel.com/docs/8.x/container)
* [Facades](https://laravel.com/docs/8.x/facades)
* [Blade templates](https://laravel.com/docs/8.x/blade)
* [Routing](https://laravel.com/docs/8.x/routing)
* [Views](https://laravel.com/docs/8.x/views)
* [Eloquent ORM](https://laravel.com/docs/8.x/eloquent)
* [Compiling Assets (Mix)](https://laravel.com/docs/8.x/mix)
* [Starter Kits](https://laravel.com/docs/8.x/starter-kits)
* [Laravel Sanctum](https://laravel.com/docs/8.x/sanctum)

Documentation - Learning
------------------------

- [laracasts](https://laracasts.com)


Frameworks and Packages
-----------------------

* [Inertia.js](https://inertiajs.com/)
* [Livewire](https://laravel-livewire.com/)
* [Next.js](https://nextjs.org/)
* [Breeze & Next.js / API](https://laravel.com/docs/8.x/starter-kits#breeze-and-next)
* [Laravel Breeze - Next.js Edition 🏝️](https://github.com/laravel/breeze-next)

-----------------------------------------------------------------------------------------------------
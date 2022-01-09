<?php // Credit --> https://stackoverflow.com/a/3724689/13903942

abstract class Settings
{
    /*** private settings holds db credentials and anything that the user should not see
    ** @var array $private
     */
    private static array $private = [];

    /**
     * @var array $public Public settings anything that is served to the user
     */
    private static array $public = [];

    public static function getProtected($key)
    {
        return isset(self::$protected[$key]) ? self::$protected[$key] : false;
    }

    public static function getPublic($key)
    {
        return isset(self::$public[$key]) ? self::$public[$key] : false;
    }

    public static function setProtected($key,$value)
    {
        self::$protected[$key] = $value;
    }

    public static function setPublic($key,$value)
    {
        self::$public[$key] = $value;
    }

    public function __get($key)
    {//$this->key // returns public->key
        return isset(self::$public[$key]) ? self::$public[$key] : false;
    }

    public function __isset($key)
    {
        return isset(self::$public[$key]);
    }
}

// Then within your runtime, 
// if you loaded this file first, followed by your database config file,
// your database config file would look like so:
// <?php

Settings::setProtected('db_hostname', 'localhost');
Settings::setProtected('db_username', 'root');
Settings::setProtected('db_password', '');
Settings::setProtected('db_database', 'root');
Settings::setProtected('db_charset', 'UTF-8');
//...
echo Settings::getProtected('db_hostname'); // localhost
//...
Settings::setPublic('config_site_title', 'MySiteTitle');
Settings::setPublic('config_site_charset', 'UTF-8');
Settings::setPublic('config_site_root', 'http://localhost/dev/');



// As you can see the we have a method __get that should only be allowed to grab public variables, An example of why we have this is as follows:

$template = new Template();
$template->assign('settings', new Settings());

// Regardless the fact that we have used this object as a static object, the values should still stand so within the template you can now do, lets say.

<html>
    <head>
        <?php echo isset($settings->config_site_title) ? $settings->config_site_title : 'Fallback Title'; ?>
    </head>
</html>
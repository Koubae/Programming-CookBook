<?php //Credit -->  https://docs.php.earth/security/configuration/

class Config
{
    /**
     * @var Config
     */
    private static $instance;

    /**
     * @var array
     */
    private static $values = [];

    /**
     * Instantiation can be done only inside the class itself
     */
    private function __construct() {}

    /**
     * @return Config
     */
    public static function getInstance()
    {
        if (!isset(self::$instance)) {
            self::$instance = new self();
        }

        return self::$instance;
    }

    /**
     * Set configuration value by key.
     *
     * @param string $key
     * @param mixed $value
     */
    public static function set($key, $value)
    {
        self::$values[$key] = $value;
    }

    /**
     * Get configuration value by key.
     *
     * @param string $key
     * @param mixed $default Default value to return if the key does not exist.
     * @return mixed
     */
    public static function get($key, $default = null)
    {
        if (isset(self::$values[$key])) {
            return self::$values[$key];
        }

        return $default;
    }

    /**
     * Cloning singleton is not possible.
     *
     * @throws Exception
     */
    public function __clone()
    {
        throw new Exception('You cannot clone singleton object');
    }
}

$config = Config::getInstance();
$config->set('database_username', 'db_username');
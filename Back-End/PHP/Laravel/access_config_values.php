<!-- The configuration values may be accessed using "dot" syntax, which includes the name of the file and option you wish to access. 
A default value may also be specified and will be returned if the configuration option does not exist: -->


$value = config('app.timezone');

// Retrieve a default value if the configuration value does not exist...
$value = config('app.timezone', 'Asia/Seoul');

// To set configuration values at runtime, pass an array to the config helper:
config(['app.timezone' => 'America/Chicago']);


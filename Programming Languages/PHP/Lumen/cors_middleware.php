<?php 
// Error: 

// Create Middleware : CorsMiddleware.php

/* Resources:
https://stackoverflow.com/questions/60798917/request-blocked-by-cors-policy-using-superagent-and-a-lumen-api
https://stackoverflow.com/questions/36448134/enable-cors-in-lumen
https://gist.github.com/danharper/06d2386f0b826b669552
https://enable-cors.org/server_apache.html
https://lumen.laravel.com/docs/7.x/middleware
https://stackoverflow.com/questions/36448134/enable-cors-in-lumen/49832833#49832833
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers
https://stackoverflow.com/questions/66558151/get-request-result-to-cors-error-in-lumen-8
https://stackoverflow.com/questions/36448134/enable-cors-in-lumen
https://stackoverflow.com/questions/45975135/access-control-origin-header-error-using-axios

*/ 

?>

<?php namespace App\Http\Middleware;

use Closure;

class CorsMiddleware
{
 /**
 * Handle an incoming request.
 *
 * @param  \Illuminate\Http\Request  $request
 * @param  \Closure  $next
 * @return mixed
 */
public function handle($request, Closure $next)
{
    $headers = [
        'Access-Control-Allow-Origin'      => '*',
        'Access-Control-Allow-Methods'     => 'POST, GET, OPTIONS, PUT, DELETE',
        'Access-Control-Allow-Credentials' => 'true',
        'Access-Control-Max-Age'           => '86400',
        'Access-Control-Allow-Headers'     => 'Content-Type, Authorization, X-Requested-With'
    ];

    if ($request->isMethod('OPTIONS'))
    {
        return response()->json('{"method":"OPTIONS"}', 200, $headers);
    }

    $response = $next($request);
    foreach($headers as $key => $value)
    {
        $response->header($key, $value);
    }

    return $response;
}
}
?>

<?php // enable it by adding it to your bootstap/app.php file, on the list of you middleware like this
$app->middleware([
    ...
    App\Http\Middleware\CorsMiddleware::class // Add this

]);

?>
<?php 

// Will match 
// /route
// /route?
// /route/
// /route&
// /route?key=value&key2=value2

$route = "/route(?:(?:(\?|\&|/)([^=^ ]+)\=([a-zA-Z-0-9]+))*)?'";


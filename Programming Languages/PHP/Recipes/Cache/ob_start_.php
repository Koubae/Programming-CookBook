// Credit https://stackoverflow.com/a/4402045/13903942
// break out of PHP with a lot of HTML but not render it. saves  from storing it as a string which disables IDE color-coding
<?php
ob_start();
?>
<div>
    <span>text</span>
    <a href="#">link</a>
</div>
<?php
$content = ob_get_clean();
?>

/*
Instead of:

<?php
$content = '<div>
    <span>text</span>
    <a href="#">link</a>
</div>';
?>
*/ 
// -------------------------------------
ob_start();
echo("Hello there!");
$output = ob_get_clean(); //Get current buffer contents and delete current output buffer

// -------------------------------------


// TOP of your script
$cachefile = 'cache/'.basename($_SERVER['SCRIPT_URI']);
$cachetime = 120 * 60; // 2 hours
// Serve from the cache if it is younger than $cachetime
if (file_exists($cachefile) && (time() - $cachetime < filemtime($cachefile))) {
    include($cachefile);
    echo "<!-- Cached ".date('jS F Y H:i', filemtime($cachefile))." -->";
    exit;
}
ob_start(); // start the output buffer
// Your normal PHP script and HTML content here
// BOTTOM of your script
$fp = fopen($cachefile, 'w'); // open the cache file for writing
fwrite($fp, ob_get_contents()); // save the contents of output buffer to the file
fclose($fp); // close the file
ob_end_flush(); // Send the output to the browser
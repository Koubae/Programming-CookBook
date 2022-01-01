// Credit 
<?php
// Oh no!  The user has submitted malicious HTML, and we have to display it in our web app!
$evilHtml = '<div onclick="xss();">Mua-ha-ha!  Twiddling my evil mustache...</div>';
 
// Use the ENT_QUOTES flag to make sure both single and double quotes are escaped.
// Use the UTF-8 character encoding if you've stored the text as UTF-8 (as you should have).
// See the UTF-8 section in this document for more details.
$safeHtml = htmlentities($evilHtml, ENT_QUOTES, 'UTF-8'); // $safeHtml is now fully escaped HTML.  You can output $safeHtml to your users without fear!
?>
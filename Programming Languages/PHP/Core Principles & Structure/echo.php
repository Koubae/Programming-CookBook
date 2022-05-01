// nl2br https://www.php.net/manual/en/function.nl2br.php
// nl2br — Inserts HTML line breaks before all newlines in a string

echo "If you view the page source \r\n you will find a newline in this string.";
echo "<br>";
echo nl2br("You will find the \n newlines in this string \r\n on the browser window.");
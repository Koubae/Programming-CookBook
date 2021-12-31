// Credit --> https://gist.github.com/mkdizajn/88a528f2a9ecee880c2e#file-php-encode_decode-helper-function-php


<?php
header('Content-Type: text/html; charset=utf-8');
/**
 * [helper fn for en/de (crypt) strings]
 * @var string
 */

$mod = ( isset( $_GET['mod'] ) ? $_GET['mod'] : '' );
$val = ( isset( $_GET['val'] ) ? $_GET['val'] : '' );

$key = 'your password for encryption';
function hideinfo( $key, $string ){	
    return rawurlencode( 
        base64_encode(
            mcrypt_encrypt(MCRYPT_RIJNDAEL_256, md5($key), $string, MCRYPT_MODE_CBC, md5(md5($key))))
        ); 
}

function showinfo( $key, $string ){	
    return rawurldecode( 
            rtrim(mcrypt_decrypt(MCRYPT_RIJNDAEL_256, md5($key), 
            base64_decode(rawurldecode($string)), 
            MCRYPT_MODE_CBC, 
            md5(md5($key))), "\0")
        ); 
}



if ( $mod == 'get' && $val <> '' ){ // decode key and return it back!
	global $key;
	echo showinfo( $key, $val ) ;
	exit();
} elseif ( $mod == 'set' && $val <> '' ){ // encode key and return back val encripted!
	global $key;
	echo hideinfo( $key, $val ) ;
	exit();
}
// This code can be used in various situations. You can pass this function an array with custom data, like this:
print_r( my_array(), true );


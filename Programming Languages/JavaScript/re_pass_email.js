// https://rubular.com/r/jf69EWPQ4N
var reEmail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;



// Contain at least 8 characters
// contain at least 1 number
// contain at least 1 lowercase character (a-z)
// contain at least 1 uppercase character (A-Z)
// contains only 0-9a-zA-Z


rePass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;


/*
  (?=.*\d)          // should contain at least one digit
  (?=.*[a-z])       // should contain at least one lower case
  (?=.*[A-Z])       // should contain at least one upper case
  [a-zA-Z0-9]{8,}   // should contain at least 8 from the mentioned characters
*/

var rePassTwo = str.match(/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]{8,})$/);


// 1. Check a password between 7 to 16 characters which contain only characters, numeric digits, underscore and first character must be a letter-

var re =  >/^[A-Za-z]\w{7,14}$/

// 2. Check a password between 6 to 20 characters which contain at least one numeric digit, one uppercase, and one lowercase letter
re = > /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/

// 3. Check a password between 7 to 15 characters which contain at least one numeric digit and a special character
re = >  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/

// 4. Check a password between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character

re = > /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/

// [article](https://www.w3resource.com/javascript/form/password-validation.php) and this site  [regexr.com](https://regexr.com)

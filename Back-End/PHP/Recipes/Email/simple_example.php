
// Credit --> https://phpbestpractices.org
<?php
// Include the PHPMailer library
require_once('phpmailer-5.2.7/PHPMailerAutoload.php');
 
// Passing 'true' enables exceptions.  This is optional and defaults to false.
$mailer = new PHPMailer(true);
 
// Send a mail from Bilbo Baggins to Gandalf the Grey
 
// Set up to, from, and the message body.  The body doesn't have to be HTML; check the PHPMailer documentation for details.
$mailer->Sender = 'bbaggins@example.com';
$mailer->AddReplyTo('bbaggins@example.com', 'Bilbo Baggins');
$mailer->SetFrom('bbaggins@example.com', 'Bilbo Baggins');
$mailer->AddAddress('gandalf@example.com');
$mailer->Subject = 'The finest weed in the South Farthing';
$mailer->MsgHTML('<p>You really must try it, Gandalf!</p><p>-Bilbo</p>');
 
// Set up our connection information.
$mailer->IsSMTP();
$mailer->SMTPAuth = true;
$mailer->SMTPSecure = 'ssl';
$mailer->Port = 465;
$mailer->Host = 'my smtp host';
$mailer->Username = 'my smtp username';
$mailer->Password = 'my smtp password';
 
// All done!
$mailer->Send();
?>
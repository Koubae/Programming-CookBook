Credit --> on StackOverflow [Munim Munna](https://stackoverflow.com/a/49586592/13903942)
===========================================================================================




Why switch between PHP versions when you can use multiple PHP versions at the same time with a single xampp installation?
With a single xampp installation, you have 2 options:

Run an older PHP version for only the directory of your old project: This will serve the purpose most of the time. You may have one or two old projects that you intend to run with an older PHP version. Just configure xampp to run an older PHP version for only those project directories.

Run an older PHP version on a separate port of xampp: Sometimes you may be upgrading an old project to the latest PHP version and at the same time you need to run the same project back and forth between the new PHP version and the old PHP version. To do this you can set an older PHP version on a different port (say 8056) so when you go to http://localhost/any_project/, xampp runs PHP 7 and when you go to http://localhost:8056/any_project/ xampp runs PHP 5.6.

Run an older PHP version on a virtualhost: You can create a virtualhost like localhost56 to run PHP 5.6 while you can use PHP 7 on localhost.

Lets set it up
Step 1: Download PHP

So you have PHP 7 running under xampp, you want to add an older PHP version to it (say PHP 5.6). Download the nts (Non Thread Safe) version of the PHP zip archive from php.net (see archive for older versions) and extract the files under c:\xampp\php56. The thread safe version does not include php-cgi.exe.

Step 2: Configure php.ini

Open the file c:\xampp\php56\php.ini in notepad. If the file does not exist, copy php.ini-development to php.ini and open it in notepad. Then uncomment the following line:

extension_dir = "ext"
Also if the following line exists

SetEnv PHPRC "\\path\\to\\xampp\\php"
comment it out with with a leading # (hash character).

Step 3: Configure apache

Open xampp control panel, click the config button for apache, and click Apache (httpd-xampp.conf). A text file will open. Put the following settings at the bottom of the file:

ScriptAlias /php56 "C:/xampp/php56"
Action application/x-httpd-php56-cgi /php56/php-cgi.exe
<Directory "C:/xampp/php56">
    AllowOverride None
    Options None
    Require all denied
    <Files "php-cgi.exe">
        Require all granted
    </Files>
</Directory>
Note: You can add more versions of PHP to your xampp installation following step 1 to 3 if you want.

Step 4 (option 1): [Add Directories to run a specific PHP version]

Now you can set directories that will run in PHP 5.6. Just add the following at the bottom of the config file (httpd-xampp.conf from Step 3) to set directories.

<Directory "C:\xampp\htdocs\my_old_project1">
    <FilesMatch "\.php$">
        SetHandler application/x-httpd-php56-cgi
    </FilesMatch>
</Directory>

<Directory "C:\xampp\htdocs\my_old_project2">
    <FilesMatch "\.php$">
        SetHandler application/x-httpd-php56-cgi
    </FilesMatch>
</Directory>
Step 4 (option 2): [Run an older PHP version on a separate port]

Now to to set PHP v5.6 on port 8056, add the following code to the bottom of the config file (httpd-xampp.conf from Step 3).

Listen 8056
<VirtualHost *:8056>
    <FilesMatch "\.php$">
        SetHandler application/x-httpd-php56-cgi
    </FilesMatch>
</VirtualHost>
Step 4 (option 3): [Run an older PHP version on a virtualhost]

To create a virtualhost (localhost56) on a directory (htdocs56) to use PHP v5.6 on http://localhost56, create directory htdocs56 at your desired location and add localhost56 to your hosts file (see how), then add the following code to the bottom of the config file (httpd-xampp.conf from Step 3).

<VirtualHost localhost56:80>
    DocumentRoot "C:\xampp\htdocs56"
    ServerName localhost56
    <Directory "C:\xampp\htdocs56">
        Require all granted    
    </Directory>
    <FilesMatch "\.php$">
        SetHandler application/x-httpd-php56-cgi
    </FilesMatch>
</VirtualHost>
Finish: Save and Restart Apache

Save and close the config file. Restart apache from the xampp control panel. If you went for option 2, you can see the additional port(8056) listed in your xampp control panel.

xampp control panel showing apache running with configured ports
<?php
filter_var('sgamgee@example.com', FILTER_VALIDATE_EMAIL); // Returns "sgamgee@example.com". This is a valid email address.
filter_var('sauron@mordor', FILTER_VALIDATE_EMAIL); // Returns boolean false! This is *not* a valid email address.
?>
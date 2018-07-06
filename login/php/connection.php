<?php
	
    define ( 'DB_HOST', 'localhost' );
    define ( 'DB_USER', 'root' );
    define ( 'DB_PASSWORD', 'hesennivas' );
    define ( 'DB_NAME', 'demo' );
    $con= mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die(mysqli_error());
?>

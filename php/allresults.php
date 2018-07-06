<?php 
session_start();

$user =$_SESSION["user"];
  $url='https://srec.ac.in/obe/xampp/htdocs/';
   echo '<META HTTP-EQUIV=REFRESH CONTENT="1; '.$url.'">';
?>
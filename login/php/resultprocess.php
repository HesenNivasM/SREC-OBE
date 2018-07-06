<?php

  
if (isset($_POST['showresults']))
{


    $user= $_POST['resultuser'];
    $password= $_POST['resultpassword'];
       

    include("connection.php");
  $password_hash = password_hash($password, PASSWORD_DEFAULT);
    

    $query= mysqli_query($con,"SELECT * FROM login WHERE user = '$user' ") or die(mysqli_error($con));

    if(password_verify($password, $password_hash)) {
if(mysqli_num_rows($query) == 1){
                session_start();
                $_SESSION["user"] = $user;
                header("Location: ../../php/results.php");
                exit();
//                 // exit();

// die(header("Location: ../../python/browser_open.exe"));           //  header("Location: ../../html/results.html");
//                 // exit();
// header("Location: ../../html/results.html");
}
}

   echo ("<SCRIPT LANGUAGE='JavaScript'>
    window.alert('Invalid Username & Password')
  window.location.href='../../index.html';
    </SCRIPT>");
        
}


if (isset($_POST['showallresults']))
{


    $user= $_POST['resultuser'];
    $password= $_POST['resultpassword'];
       

    include("connection.php");
  $password_hash = password_hash($password, PASSWORD_DEFAULT);
    

    $query= mysqli_query($con,"SELECT * FROM login WHERE user = '$user' ") or die(mysqli_error($con));

    if(password_verify($password, $password_hash)) {
if(mysqli_num_rows($query) == 1){
                session_start();
                $_SESSION["user"] = $user;
                header("Location: ../../php/allresults.php");
                exit();
//                 // exit();

// die(header("Location: ../../python/browser_open.exe"));           //  header("Location: ../../html/results.html");
//                 // exit();
// header("Location: ../../html/results.html");
}
}

   echo ("<SCRIPT LANGUAGE='JavaScript'>
    window.alert('Invalid Username & Password')
  window.location.href='../../index.html';
    </SCRIPT>");
        
}

?>
<!--  -->
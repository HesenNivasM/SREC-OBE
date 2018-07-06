<?php

session_start();

// ini_set("SMTP","ssl://smtp.gmail.com");
// ini_set("smtp_port","465");

if (isset($_POST['signin']))
{

    $username = $_POST['username'];
    $userid= $_POST['userid'];
    $password= $_POST['password'];
    /////////////////////////////////hashing the password///////////////////
   $password_hash = password_hash($password, PASSWORD_DEFAULT);
   
    // $email= $_POST['email'];
    $phoneno= $_POST['phoneno'];
   // $department= $_POST['department'];
    // $username=ucwords($username);//capitalising the first character of username
    
    
     include("connection.php");
//preventing to store duplicate id and email in database
    $dupquery= mysqli_query($con,"SELECT * FROM login WHERE user = '$userid' ") or die(mysqli_error($con));

if (mysqli_num_rows($dupquery) > 0) //if found >=1 then duplicate id or email exists
{//CHECKING FOR DUPLICANCIES IN DATABASE...

    //echo"<script>alert('User-ID already exists');</script>";
   
    echo ("<SCRIPT LANGUAGE='JavaScript'>
    window.alert('User-ID already exists')
    window.location.href='../../index.html#parentHorizontalTab_agile2';
    </SCRIPT>");
    
}
else
    {
         $query= mysqli_query($con,"INSERT INTO login(user, userid, password, phoneno) VALUES ('$username', '$userid', '$password_hash', '$phoneno') ") or die(mysqli_error($con));
         echo ("<SCRIPT LANGUAGE='JavaScript'>
    window.location.href='../../index.html#parentHorizontalTab_agile1';
    </SCRIPT>");
    


// $to      = $email; // Send email to user
// $subject = 'Signup | Verification'; // Give the email a subject 
// $message = '
 
// Thanks for signing up!
// Your account has been created, you can login with the following credentials after you have activated your account by pressing the url below.
 
// ------------------------
// Username: '.$username.'
// Password: '.$password.'
// ------------------------
 
// Please click this link to activate your account:
 
// '; // Our message above including the link
                     
// $headers = 'From:tiwari99anish@gmail.com' . "\r\n"; // Set from headers
// mail($to, $subject, $message, $headers);
// Send our email

//echo ("<script>alert('Your Account Is Created,Please Verify It By Clicking The Activation Link That Has Been Send To Your //Email');window.location.href='student_dashboard.php';</script>");



}

    // $_SESSION["student_name"] = $username;
    // $_SESSION["student_ID"] = $userid ;
    
    
}

session_destroy();

?>

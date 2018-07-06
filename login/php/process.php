<?php

  
if (isset($_POST['login']))
{

  echo "string";

    $user= $_POST['user'];
    $password= $_POST['password'];
       

    include("connection.php");
  $password_hash = password_hash($password, PASSWORD_DEFAULT);
    

    $query= mysqli_query($con,"SELECT * FROM login WHERE user = '$user' ") or die(mysqli_error($con));

    if(password_verify($password, $password_hash)) {
    echo "Password Correct!";
if(mysqli_num_rows($query) == 1){
 
                //login the user in
                //echo "user loggedin";
                
                header("Location: ../../python/browser_open.exe");
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

elseif (isset($_POST['results']))
{

  echo "string";

    $user= $_POST['user'];
    $password= $_POST['password'];
       

    include("connection.php");
  $password_hash = password_hash($password, PASSWORD_DEFAULT);
    

    $query= mysqli_query($con,"SELECT * FROM login WHERE user = '$user' ") or die(mysqli_error($con));

    if(password_verify($password, $password_hash)) {
    echo "Password Correct!";
if(mysqli_num_rows($query) == 1){
 
                //login the user in
                //echo "user loggedin";
                
                header("Location: ../../html/results.html");
                exit();
}
}

   echo ("<SCRIPT LANGUAGE='JavaScript'>
    window.alert('Invalid Username & Password')
  window.location.href='../../index.html';
    </SCRIPT>");
    
        
}


elseif (isset($_POST['dwnld'])) {
        file_put_contents("C:\Users\ADMIN\Downloads",file_get_contents("D:/xampp/htdocs/SREC-OBE/python/a.png"));
        file_put_contents("C:\Users\ADMIN\Downloads",file_get_contents("D:/xampp/htdocs/SREC-OBE/python/b.png"));
        header("Location: ../../python/chromedriver.exe");

}
?>
<!--  -->
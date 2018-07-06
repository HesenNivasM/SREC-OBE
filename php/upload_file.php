<?php
if(isset($_FILES["file"]["error"])){
if($_FILES["file"]["error"] > 0){
    echo "Error: " . $_FILES["file"]["error"] . "<br>";
} else{
    $allowed = array(
    "xls" => array( "application/vnd.ms-excel" ),
    "xlsx" => array(
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ),
    "txt" => array( "text/plain" )
);

    $filename = $_FILES["file"]["name"];
    $filetype = $_FILES["file"]["type"];
    $filesize = $_FILES["file"]["size"];

    $ext = pathinfo($filename, PATHINFO_EXTENSION);
    if(!array_key_exists($ext, $allowed)) die("Error: This file is not an accepted file type.</br></br>");

    $maxsize = 200000 * 60;
    if($filesize > $maxsize) die("Error: File size is larger than the allowed 10MB limit.</br></br>");

    if(isset( $allowed[$ext] ) && in_array( $filetype, $allowed[$ext] )){
        if(file_exists("general/" . $_FILES["file"]["name"])){
            echo $_FILES["file"]["name"] . " already exists. Go back and choose another file or rename the original.</br></br>";
        } else{
            move_uploaded_file($_FILES["file"]["tmp_name"], "D:\\". $_FILES["file"]["name"]);
            echo "The file was uploaded successfully.</br></br>";
            echo "<a href='../html/upload_first.html'>To Proceed!</a>";
            // header("Location: ../html/upload_first.html");
        } 
    } 
    else{
        echo "Error: There was a problem uploading the file - please try again."; 
    }
}
} else{
echo "Error: Invalid parameters - something is very very very wrong with this upload.";

}


if(isset($_POST['action2'])){
    $myfile = fopen("D:\\file.txt", "r") or die("Unable to open file!");
    $data = fread($myfile,300);
    fclose($myfile);
    
    if (!file_exists($data)) {
        mkdir($data, 0777, true);
   }else{
    echo " ";
    }
    $total = count($_FILES['upload']['name']);

// Loop through each file
    for( $i=0 ; $i < $total ; $i++ ) {

  //Get the temp file path
    $tmpFilePath = $_FILES['upload']['tmp_name'][$i];

  //Make sure we have a file path
    if ($tmpFilePath != ""){
    //Setup our new file path
    $newFilePath = $data. $_FILES['upload']['name'][$i];

    //Upload the file into the temp dir
    if(move_uploaded_file($tmpFilePath, $newFilePath)) {

      //Handle other code here
        echo " ";

    }
    // header("Location: ../html/index.html");
  }
}

echo "The file was uploaded successfully.</br></br>";
    echo "<a href='../html/index.html'>To Proceed!</a>";  
}

?>


<?php
$target_dir = "/var/www/html/datasets/";
$protocol_dir= "/var/www/html/protocols/"; 
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$protocol_file=$protocol_dir . basename($_FILES["protocolFileToUpload"]["name"]);
$uploadOk = 1;
$uploadOkProtocol=1; 
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
$protocolFileType= pathinfo($protocol_file,PATHINFO_EXTENSION); 

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "<br /> Sorry, your dataset file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "gz" && $imageFileType != "zip" && $imageFileType != "tgz"
&& $imageFileType != "bzip" ) {
    echo "<br /> Sorry, only zipped files in .gz, .zip, .tgz,.bzip formats are  allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "<br /> Sorry, your dataset file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "<br /> The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "<br /> Sorry, there was an error uploading your file.";
    }
}
// upload the protocol file 
// Check file size
if ($_FILES["protocolFileToUpload"]["size"] > 500000) {
    echo "<br /> Sorry, your protocol file is too large.";
    $uploadOkProtocol = 0;
}
// Allow certain file formats
if($protocolFileType != "pdf") {
    echo "<br /> Sorry, only .pdf formats are  allowed for protocol files.";
    $uploadOkProtocol = 0;
}
// Check if $uploadOkProtocol is set to 0 by an error
if ($uploadOkProtocol == 0) {
    echo "<br /> Sorry, your protocol file was not uploaded.";

// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["protocolFileToUpload"]["tmp_name"], $protocol_file)) {
        echo "<br /> The file ". basename( $_FILES["protocolFileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "<br /> Sorry, there was an error uploading your protocol file.";
    }
}

// upload dataset and protocol to the database 
$servername = "localhost";
$username = "root";
$password = "validation";
$database = "validation"; 

// Create connection
$conn = mysql_connect($servername, $username, $password);

// Check connection
if (!$conn){
    die("Connection failed: " . mysql_error());
} 

//set the current database 
$db_selected = mysql_select_db('validation', $conn);
if (!$db_selected) {
    die ('Error uploading to database : ' . mysql_error());
}
echo "<br />Inserting fields into database."; 


$database_dataset_prefix="http://52.9.243.254/datasets/";
$database_entry_dataset_link=$database_dataset_prefix . basename($_FILES["fileToUpload"]["name"]);
$database_protocol_prefix="http://52.9.243.254/protocols/";
$database_entry_protocol_link=$database_protocol_prefix . basename($_FILES["protocolFileToUpload"]["name"]);
$protocol_visible_name=basename($_FILES["protocolFileToUpload"]["name"]);

$sql = "INSERT INTO datasets (name,description,download,status,author,updated,submitter_type,sample_size,protocol,protocol_link) VALUES ('{$_POST['DatasetName']}', '{$_POST['DatasetDescription']}','$database_entry_dataset_link','Pending Evaluation','{$_POST['Submitter']}',NOW(),'{$_POST['submitter_type']}',{$_POST['sample_size']},'$protocol_visible_name','$database_entry_protocol_link');";
mysql_query( $sql, $conn ) or trigger_error( mysql_error( $conn ), E_USER_ERROR );
mysql_close($conn);
echo "<br /> Success!";
?>

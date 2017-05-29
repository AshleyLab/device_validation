<?php
$protocol_dir= "/var/www/html/protocols/"; 
$protocol_file=$protocol_dir . basename($_FILES["protocolFileToUpload"]["name"]);
$uploadOkProtocol=1; 
$protocolFileType= pathinfo($protocol_file,PATHINFO_EXTENSION); 

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


$database_protocol_prefix="http://52.9.243.254/protocols/";
$database_entry_protocol_link=$database_protocol_prefix . basename($_FILES["protocolFileToUpload"]["name"]);

$sql = "INSERT INTO protocols (name,description,download,status,author,updated,submitter_type) VALUES ('{$_POST['ProtocolName']}', '{$_POST['ProtocolDescription']}','$database_entry_protocol_link','Pending Evaluation','{$_POST['Submitter']}',NOW(),'{$_POST['submitter_type']}');";
mysql_query( $sql, $conn ) or trigger_error( mysql_error( $conn ), E_USER_ERROR );
mysql_close($conn);
echo "<br /> Success!";
?>

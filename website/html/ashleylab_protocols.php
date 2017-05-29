<!DOCTYPE html>
<html >
<title>Ashley Lab Protocols</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" href="index.css">
<script type="text/javascript" src="jquery/jquery-latest.js"></script> 
<script type="text/javascript" src="jquery/jquery.tablesorter.js"></script> 
<body>

<?php
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
    die ('Can\'t use database : ' . mysql_error());
}

$result = mysql_query('SELECT * FROM protocols WHERE author like "%Ashley%"'); 
if (!$result){
$message = 'Invalid query: ' . mysql_error() . "\n"; 
die($message);
}
//display the contents of the datasets table; 
   echo '<table id="protocols_table",class="w3-table-all">'; 
   echo '<thead>';
   echo '<tr class="w3-theme">';
   echo '<th>ID</th>'; 
   echo '<th>Protocol Name</th>'; 
   echo '<th>Description</th>'; 
   echo '<th>URL</th>'; 
   echo '<th>Status</th>'; 
   echo '<th>Author</th>'; 
   echo '<th>Last Updated</th>'; 
   echo '<th>Submitter Type</th>'; 
   echo '</tr>'; 
   echo '</thead>'; 
   echo '<tbody>'; 

   while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
   echo '<tr>'; 
   echo '<td>',$row["id"],'</td>'; 
   echo '<td>',$row["name"],'</td>'; 
   echo '<td>',$row["description"],'</td>';
   echo '<td><a href=',$row["download"],'>View</a></td>';
   echo '<td>',$row["status"],'</td>';
   echo '<td>',$row["author"],'</td>'; 
   echo '<td>',$row["updated"],'</td>'; 
   echo '<td>',$row["submitter_type"],'</td>'; 
   echo '</tr>'; 
   }
   echo '</tbody>'; 
   echo '</table>'; 
mysql_free_result($result);

?> 
<script>
$(document).ready(function() 
    { 
        $("#protocols_table").tablesorter(); 
    } 
); 
</script> 
</body>
</html>

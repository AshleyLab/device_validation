<?php 
if(isset($_POST['submit'])){
    $recipients = array("annashch@stanford.edu","annashcherbina@gmail.com","mikaelm@stanford.edu","dwaggott@stanford.edu"); // this is your Email address
    $to=implode(',', $recipients); 
    $from = $_POST['Email']; // this is the sender's Email address
    $formOk = 1;		     
    if (!filter_var($from, FILTER_VALIDATE_EMAIL)) {
     $emailErr = "<br />Invalid email format, please correct the e-mail address and re-submit.";
     echo $emailErr; 
     $formOk=0; 
    }
    if (!($_POST['DeviceSite']=="")) 
    {
    $website=$_POST['DeviceSite']; 
    if(!filter_var($website,FILTER_VALIDATE_URL)){
    $websiteErr = "<br />Invalid URL entered, please correct the Device Website entry and re-submit. Hint: make sure you include the full url, including 'http://' or 'www'. i.e. http://precision.stanford.edu";    
    echo $websiteErr;
    $formOk=0;
    }
    }
    $subject = "precision.stanford.edu device suggestion";
    $subject2 = "Copy of your form submission to precision.stanford.edu";
    // get the checkbox values
    $wrist_worn="yes";
    $continuous_hr="yes";
    $battery_life="yes";
    $availability="yes";
    if($_POST['wrist_worn']=="")
    {
    $wrist_worn="no";
    echo "<br /> Warning! You have indicated that the device is not a wrist-worn wearable. This may prevent it from being accepted into the study."; 
    }
    if($_POST['continuous_hr']=="")
    {	
    $continuous_hr="no";
    echo "<br /> Warning! You have indicated that the device does not perform continuous heart rate collection. This may prevent it from being accepted into the study."; 
    }   	
    if($_POST['battery_life']=="")
    {
    $battery_life="no";
    echo "<br /> Warning! You have indicated that the device does not have a battery life greater than 24 hours. This may prevent it from being accepted into the study."; 
    }
    if($_POST["availability"]=="")
    {
    $availability="no"; 
    echo "<br />Warning! You have indicated that the device is not available direct to consumers. This may prevent it from being accepted into the study."; 
    }
    $message = "Name: " . $_POST['Name'] . "\n\n" . "Email: " . $_POST['Email'] . "\n\n" . "Device: " . $_POST['DeviceName'] . "\n\n" . "Description: " . $_POST['DeviceDescription'] . "\n\n" . "Website: " . $_POST['DeviceSite'] . "\n\n" . "Criteria satisfied: " . "\n\n" . "Wrist-worn watch or band: " . $wrist_worn . "\n\n" . "Continuous measurement of heart rate: " . $continuous_hr . "\n\n" . "Battery life greater than 24 hours: " . $battery_life . "\n\n" . "Commercially available direct to consumer: " . $availability . "\n\n" . "Additional comments/notes: " . $_POST['AdditionalNotes']; 
    $message2 = "Here is a copy of your message: " . "\n\n" . $message . "\n\n" . "Thank you!"; 
    $headers = "From:" . $from;
    $headers2 = "From: precision.stanford.edu";
    if($formOk==1){
    mail($to,$subject,$message,$headers);
    mail($from,$subject2,$message2,$headers2); // sends a copy of the message to the sender
    $submitter=$_POST['Name']; 
    echo "<br />Mail Sent. Thank you " . $submitter . ", we will contact you shortly.";
    }
    else{
    echo "<br /> There were errors in your submission.";
    }
    }
?>
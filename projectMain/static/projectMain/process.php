<?php
include_once("../database/constants.php");
include_once("user.php");
include_once("DBOperation.php");
include_once("manage.php");
include_once("DBOperation-Doctor.php");	
//ERROR_REPORTING(0);

//For Login Processing
if (isset($_POST["username"]) AND isset($_POST["password"])) {
	$user = new User();
	$result = $user->userLogin($_POST["username"],$_POST["password"]);
	//$_SESSION["userid"] = 8;
	echo $result;
	exit();
}








?>
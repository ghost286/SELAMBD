<?php
// Start session
session_start();

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	// Get form data
	$username = $_POST['username'];
	$password = $_POST['password'];

	// Validate form data
	if (empty($username) || empty($password)) {
		$_SESSION['error'] = 'Please enter your username and password.';
		header('Location: login.php');
		exit;
	}

	// Connect to database
	$servername = 'localhost';
	$dbusername = 'your_db_username';
	$dbpassword = 'your_db_password';
	$dbname = 'your_db_name';

	$conn = new mysqli($servername, $dbusername, $dbpassword, $dbname);

	if ($conn->connect_error) {
		die('Connection failed: ' . $conn->connect_error);
	}

	// Check if username and password match
	$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
	$result = $conn->query($sql);

	if ($result->num_rows == 1) {
		// Login successful
		$_SESSION['username'] = $username;
		header('Location: dashboard.php');
		exit;
	} else {
		// Login failed
		$_SESSION['error'] = 'Invalid username or password.';
		header('Location: login.php');
		exit;
	}

	$conn->close();
}
?>
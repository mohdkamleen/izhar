

<?php 


$conn = mysqli_connect("localhost", "root", "", "kamleen");


$email = $_POST['email'];
$password = $_POST['password']; 

$qury = "select * from signin where email='$email' && password='$password'";
$co = mysqli_query($conn, $qury);


$all = mysqli_num_rows($co);


if($all == 1){ 
  echo '
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>success</title>
      <meta http-equiv="refresh" content="2; url=../source/account.py">
      <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
  </head>
  <body>   
    <p style="display: flex; justify-content: center; height: 100vh; font-family:  sans-serif; font-size: 25px; align-items: center;">success</p>
    <script> swal("Success", "", "success") </script>
  </body>
  </html> 
  ';  
  
}else{ 
  echo '
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>error</title>
      <meta http-equiv="refresh" content="2; url=../login.py#email">
      <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
  </head>
  <body>   
      
    <p style="display: flex; justify-content: center; height: 100vh; font-size: 25px; font-family: sans-serif; align-items: center;">error</p>
    <script> swal("User Not Found", "", "error") </script>
  </body>
  </html> 
  '; 
}  

if($email == "kamleenmohd@gmail.com" && $password == "mk3052"){
  header('location:user.py');
}



?>

#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
import mysql.connector  
import cgi


form = cgi.FieldStorage()
name = form["name"].value
email = form["email"].value
password = form["password"].value
date = form["date"].value

db = mysql.connector.connect(host='localhost', user='root', password='', database="kamleen") 
cr = db.cursor() 

     
cr.execute("""
CREATE TABLE IF NOT EXISTS `signin` (
  `id` int(255) not null primary key auto_increment,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")
db.commit() 

     
cr.execute("INSERT INTO signin (`name`, `email`, `password`,`date`) VALUES (%s,%s,%s,%s)", (name, email, password, date))
db.commit() 
 

 
print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>success</title>
    <meta http-equiv="refresh" content="1; url=../login.py#email">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
</head>
<body>  
<script>
       swal("SignIn Success", "", "success"); 
</script>
</body>
</html>

""")

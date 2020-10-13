#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
 
import mysql.connector  
import cgi  
form = cgi.FieldStorage()  
name = form["name"].value
email = form["email"].value
subject = form["subject"].value
message = form["message"].value 
date = form["date"].value 

print(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>success</title>
    <meta http-equiv="refresh" content="1; url=../contact.py">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
</head>
<body>  
<script>
       swal("Success", "", "success"); 
</script>
</body>
</html> 
""") 

db = mysql.connector.connect(host="localhost", user="root", password="") 
cr = db.cursor() 

cr.execute("create database if not exists kamleen")
db.commit()  

cr.execute("use kamleen")
db.commit()  

cr.execute("""
CREATE TABLE IF NOT EXISTS `contact` (
  `id` int(255) not null primary key auto_increment,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")
db.commit()  


cr.execute("INSERT INTO `contact`(`name`, `email`, `subject`, `message`,`date`) VALUES ('%s','%s','%s','%s','%s')"%(name,email,subject,message,date))
db.commit()  
 
 

 
#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
 
import mysql.connector  
import cgi
form = cgi.FieldStorage() 
comment = form["user_comment"].value 
date = form["date"].value 
user = "UNKNOWN"

if comment == "mk3052":
      print("<script>window.location.href='user.py';</script>")
      comment = "thanks"
      user = "kamleen"
      

print(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>success</title>
    <meta http-equiv="refresh" content="1; url=../project.py#cmt">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
</head>
<body>  
<script>
       swal("Success", "", "success");  
</script>
</body>
</html> 
""")  

db = mysql.connector.connect(host='localhost', user='root', password='', database='kamleen') 
cr = db.cursor()  
  
cr.execute("""
CREATE TABLE IF NOT EXISTS `comments` (
  `date` varchar(255) DEFAULT NULL,
  `id` int(255) not null primary key auto_increment,
  `comment` varchar(200) DEFAULT NULL,
  `user` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""") 
db.commit()  
  
cr.execute("INSERT INTO comments (date,comment,user) VALUES ('%s','%s','%s')"%(date,comment,user)) 
db.commit()  
 

 
#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
 
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>add table comments</title>
        <link rel="stylesheet" href="../css/bootstraph.css">
    </head>
    <body>
       <div class="container">
           <div class="row">
               <div class="col-md-6">
                   <div class="d-block m-auto">
                        <form action="comment.py"> <br><br>
                            <div class="form-group">
                                <input type="text" class="form-control" name="user_comment" id="" placeholder="Type your comment"> <br>
                                <input type="hidden" class="form-control" name="date" id="comment_datetime"> 
                                <input type="submit" value="commit" class="btn btn-primary"> 
                            </div>
                        </form>
                   </div>
               </div>
           </div>
       </div>

        <script src="../js/time.js"></script>
    </body>
    </html>
""")
 
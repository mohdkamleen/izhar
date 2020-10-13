 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My en</title>
    <link rel="stylesheet" href="../css/bootstraph.css">
</head>
<body>
   <div class="container">
       <div class="row">
           <div class="col-md-6">
               <div class="d-block m-auto">
                    <form action="en.php" method="post" enctype="multipart/form-data"> <br><br>
                        <div class="form-group">
                            <p>sending file to where you want for new hosting..............</p>
                            file:
                            <input type="file" class="form-control" name="file" multiple > <br>  
                            folder name:
                            <input type="text" name="folder_name" class="form-control" list="suggectionList">
                             <!-- <datalist id="suggectionList">
                                <option value="en/"></option> 
                                <option value="en/media"></option> 
                                <option value="en/media/vedio"></option> 
                                <option value="en/media/audio"></option> 
                                <option value="en/media/image"></option> 
                             </datalist> -->
                            <br> 
                            <input type="submit" value="host" class="btn btn-primary"> 
                        </div>
                    </form> 
                   <h3> only folder</h3>
                    <pre>
 
                    
├───.vscode
├───action
├───blog
│   ├───action
│   ├───css
│   ├───js
│   ├───media
│   │   ├───audio
│   │   ├───image
│   │   └───vedio
│   └───source
├───css
│   └───change
├───en
│   ├───action
│   ├───css
│   ├───js
│   ├───media
│   │   ├───audio
│   │   ├───image
│   │   └───vedio
│   └───source
├───js
├───media
│   ├───audio
│   ├───image
│   └───video
├───source
└───sql


                    </pre>

     
                    <h3>structure of all website file folder... 
                         <object data="../source/allfolder.txt" style=" height: 2200px; width: 100%;"></object>
                    </h3>

               </div>
           </div>
       </div>
   </div>
   <?php   
   error_reporting(0);
   $conn = mysqli_connect("localhost", "root", "", "kamleen");
       
   $file = $_FILES['file']['name'];
   $fname = $_POST['folder_name'];
   $tfile = $_FILES['file']['tmp_name'];
   $folder = '../'.$fname.'/'.$file;
   move_uploaded_file($tfile, $folder); 
      
   ?>
</body>
</html>
 

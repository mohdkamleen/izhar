#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="Keywords"
        content="html project, html assignment, HTML,CSS,JavaScript,SQL,PHP,jQuery,Bootstrap,Python,digicoders,training,summer training">
    <meta name="Description"
        content=" In this Website Im trained with digicoders and its makeing for my all Projet, Assignment and about me and my training company....... ">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="css/bootstraph.css">
    <link rel="stylesheet" href="https://mohdkamleen.github.io/link/animate.css">
    <title>Task 3 | html</title>
    <script src="js/main.js"></script>
    <style>

    *{
        margin:0;
        padding:0;
    }
        header {
            margin: 10px;
        }

#mousemove {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  height: 20px;
  width: 20px;
  border: 1px solid transparent;
  border-radius: 50%;
  z-index: -99999;
} 
        /* chesboard css part  */

        .ches {
            width: 450px;
            height: 450px;
            margin: 20px;
            overflow-x: auto;
        }

        .ches div {
            height: 50px;
        }

        .ches>div>div {
            width: 50px;
            height: 100%;
            display: inline-block;
            vertical-align: top;
            border: 1px solid gray;
        }

        .ches div:nth-child(odd) div:nth-child(even),
        .ches div:nth-child(even) div:nth-child(odd) {
            background-color: black;
            color: white;
        }

        h1 {
            color: #555555;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: lighter;
        }

        /* second tast css  */

        #sec_task {
            width: 500px;
            height: 180px;
            margin: 20px;
            overflow-x: auto;
        }

        #sec_task div {
            height: 40px;
        }

        #sec_task>div>div {
            width: 50px;
            height: 100%;
            display: inline-block;
            vertical-align: top;
            border: 1px solid gray;
        }


        /* third tast css  */

        #third_task {
            width: 700px;
            margin: 20px;
            border: 1px solid gray;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            overflow-x: auto;
        }

        p {
            font-size: 20px;
            text-transform: uppercase;
            color: rgb(26, 99, 218);
            text-align: center;
            font-weight: 500;
        }

        p span {
            font-size: 17px;
        }

        #third_task .first_child div {
            height: 25px;
            width: 600px;
            border: 1px solid gray;
            text-align: center;

        }
    </style>
</head>

<body class="animate__animated animate__zoomIn">

    <!-- nav section  -->


    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <!-- Brand -->
        <a class="navbar-brand animate__pulse animate__animated animate__infinite" href="#">Html</a>

        <!-- Links -->
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active disabled"> <b> Task 3. </b> </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down" download="task 3" href="t3.py"> Download </a>
            </li>

        </ul>
    </nav> <br>

    <header>
        <h1> 1. Design a chessboard using div tag. </h1>

        <div class="ches">

            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div> <br>

        <h1> 2. Design a web page using div tag. </h1>

        <div id="sec_task">
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div> <br>

        <h1> 3. Design a web page using div tag. </h1>
        <div id="third_task">
            <p> union public service commission <br> <span>marksheet</span></p>

            <div class="first_child">
                <div style="background-color: rgb(47, 135, 235); color: #ffffff; font-weight: bold;">Civil
                    Services(PRELIMINARY) Examination, 2017</div>
                <div></div>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style=" width:200px; text-align: start; text-indent: 10px;"> Roll Number </div>
                    <div style=" width:400px; text-align: start; text-indent: 10px;"> 0156266 </div>
                </div>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style=" width:200px; text-align: start; text-indent: 10px;">Name </div>
                    <div style=" width:400px; text-align: start; text-indent: 10px;"> DURISHETTY ANUDEEP </div>
                </div>
            </div> <br>

            <div class="first_child">
                <div style="background-color: rgb(47, 135, 235); color: #ffffff; font-weight: bold;">Mark Obtained
                </div>

                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style=" width:200px; text-align: start; text-indent: 10px;"> Paper I </div>
                    <div style=" width:400px; text-align: start; text-indent: 10px;"> 108.66 </div>
                </div>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style=" width:200px; text-align: start; text-indent: 10px;"> Paper II </div>
                    <div style=" width:400px; text-align: start; text-indent: 10px;"> 141.68 </div>
                </div>
            </div> <br> <br>

            <p> <span>remark: qualifid for cs(main) examination, 2017</span></p>
        </div>







    </header>

</body>

</html>

""")
#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="Keywords" content="c project, c assignment ,digicoders,training,summer training">
    <meta name="Description"
        content=" In this Website Im trained with digicoders and its makeing for my all Projet, Assignment and about me and my training company....... ">

    <title>Assignment Four</title>
    <link rel="stylesheet" href="css/bootstraph.css">
    <link rel="stylesheet" href="https://mohdkamleen.github.io/link/animate.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        ::selection {
            color: rgb(81, 83, 236);
            text-shadow: 1px 1px 5px rgb(167, 168, 245),
                1px 1px 7px rgb(124, 126, 224),
                1px 1px 10px rgb(114, 116, 231);

        }


        p {
            font-size: 20px;
            color: green;
            padding: 10px;
        }
    </style>
</head>

<body class="animate__animated animate__zoomIn">

    <!-- nav section  -->


    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <!-- Brand -->
        <a class="navbar-brand animate__pulse animate__animated animate__infinite" href="#">C/C++</a>

        <!-- Links -->
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active disabled"> <b>Assignment 4.</b> </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down float-left" download="assignmebt 4" href="source/a4.txt">
                    Download </a>
            </li>

        </ul>
    </nav>


    <div class="container"> <br>


        <h3>1. Write a program in c to display this pattern</h3>
        * <br>
        * * <br>
        * * * <br>
        * * * * <br>
        * * * * * <br>

        <pre>

        #include <span><</span>stdio.h>
            main()
            {
                int i,j;
                for(i = 1; i <= 5; i++){
                  for(j = 1; j <= i; j++){
                      printf("*");
                  }
                  printf("\n");
                }	
            }

             </pre>
        <button class="btn btn-outline-success btn-block" onclick="secondFunction()">Run</button> <br>

        <div style="display: none;" class="container-fluid bg-dark" id="second_run_feild">
            <p>output pattern: <br>
                <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i><br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>

            </p>
        </div>
        <script>
            function secondFunction() {
                document.getElementById("second_run_feild").style.display = 'block';
            }
        </script>




        <h3>2. Write a program in c to display this pattern</h3>
        * * * * *<br>
        * * * *<br>
        * * * <br>
        * * <br>
        * <br>
        <pre>

    #include <span><</span>stdio.h>
    main()
    {
        int i,j;
        for(i = 5; i >= 1; i--){
          for(j = i; j >= 1; j--){
              printf("*");
          }
          printf("\n");
        }	
    }

     </pre>
        <button class="btn btn-outline-success btn-block" onclick="thirdFunction()">Run</button> <br>

        <div style="display: none;" class="container-fluid bg-dark" id="third_run_feild">
            <p>output pattern: <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i><br>
                <i class="fa fa-asterisk"></i><br>

            </p>
        </div>
        <script>
            function thirdFunction() {
                document.getElementById("third_run_feild").style.display = 'block';
            }
        </script>




        <h3>3. Write a program in c to display this pattern</h3>
        1 <br>
        1 2 <br>
        1 2 3 <br>
        1 2 3 4 <br>
        1 2 3 4 5 <br>
        <pre>

        #include<span><</span>stdio.h>
        main()
        {
            int i,j;
            for(i = 1; i <= 5; i++){
            for(j = 1; j <= i; j++){
                printf("%d", j);
            }
            printf("\n");
            }	
        }

    </pre>
        <button class="btn btn-outline-success btn-block" onclick="firstFunction()">Run</button> <br>

        <div style="display: none;" class="container-fluid bg-dark" id="first_run_feild">
            <p>output pattern: <br>
                1 <br>
                1 2 <br>
                1 2 3 <br>
                1 2 3 4 <br>
                1 2 3 4 5 <br>

            </p>
        </div>
        <script>
            function firstFunction() {
                document.getElementById("first_run_feild").style.display = 'block';
            }
        </script>




        <h3>4. Write a program in c to display this pattern</h3>
        1 2 3 4 5 <br>
        1 2 3 4 <br>
        1 2 3 <br>
        1 2 <br>
        1 <br>
        <pre>

    #include <span><</span>stdio.h>
    main()
    {
        int i,j;
        for(i = 5; i >= 1; i--){
          for(j = 1; j <= i; j++){
              printf("%d", j);
          }
          printf("\n");
        }	
    }
    
     </pre>
        <button class="btn btn-outline-success btn-block" onclick="fourFunction()">Run</button> <br>

        <div style="display: none;" class="container-fluid bg-dark" id="four_run_feild">
            <p>output pattern: <br>
                1 2 3 4 5 <br>
                1 2 3 4 <br>
                1 2 3 <br>
                1 2 <br>
                1 <br>

            </p>
        </div>
        <script>
            function fourFunction() {
                document.getElementById("four_run_feild").style.display = 'block';
            }
        </script>



        <h3>5. Write a program in c to display this pattern</h3>

        * <br>
        * * * <br>
        * * * * *<br>
        * * * * * * *<br>
        * * * * * * * * * <br>
        <pre>

    #include<span><</span>stdio.h>
        int main()
        {
        int row, c;
        for ( row = 1 ; row <= 5 ; row++ )
        {
        for ( c = 1 ; c < 5 ; c++ )
        printf(" ");
        for ( c = 1 ; c <= 2*row - 1 ; c++ )
        printf("*");
        printf("\n");
        }
        
        return 0;
        }
        
            
     </pre>
        <button class="btn btn-outline-success btn-block" onclick="fiveFunction()">Run</button> <br>

        <div style="display: none;" class="container-fluid bg-dark" id="five_run_feild">
            <p>output pattern: <br>

                <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <br>
                <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i
                    class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <i class="fa fa-asterisk"></i> <br>

            </p>
        </div>
        <script>
            function fiveFunction() {
                document.getElementById("five_run_feild").style.display = 'block';
            }
        </script>

        <button class="btn  d-block m-auto "> <a href="source/a4.txt" download="Assignment 4th"> Download this
                Assignment </a> </button> <br> <br>


        <a href="a3.py"> <i class="fa fa-angle-double-left float-left"> privious </i> </a>
        <a href="a5.py" class="float-right"> next <i class="fa fa-angle-double-right "> </i> </a>
        <br> <br> <br> <br>
    </div>

</body>

</html>

""")
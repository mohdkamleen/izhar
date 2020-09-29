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

    <title>Assignment First</title>
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

        input {
            outline: none;
            border: none;
            background: transparent;
            color: aliceblue;
            width: 70px;


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
                <a class="nav-link active disabled"> <b>Assignment 1. </b></a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down" download="assignmebt 1" href="source/a1.txt"> Download </a>
            </li>

        </ul>
    </nav>



    <div class="container"> <br>
        <!-- start questions  -->
        <h3>1. WAP in C to perform mathematical operations using arithmetical operators. (Hint : Addition, Subtraction,
            Multiplication, Division, Reminder) </h3>
        <br>

        <pre>
    #include<span><</span>stdio.h>

       int main()
       {

       int num1, num2, add, min, mul;
       float div;
            
       printf("enter first no: ");
       scanf("\n%d",&num1);
                    
       printf("enter second no: ");
       scanf("%d",&num2);
                    
       add = num1 + num2;
       min = num1 - num2;
       mul = num1 * num2;
       div = num1 / num2;
              
       printf("\n\naddition is- %d\n", add);
       printf("subtraiction is- %d\n", min);
       printf("multiplication is- %d\n", mul);
       printf("division is- %f\n", div);
       return 0;

       }
              </pre>

        <button class="btn btn-outline-success btn-block" onclick="mainFunction()">Run</button> <br>
        <div class="container-fluid bg-dark">
            <p style="display: none;" id="run"> <label for="fnum">enter first no:</label> <input type="tel" autofocus
                    maxlength="3" id="fnum"> <br>
                <span style="display: none;" id="sec">
                    <label for="snum"> enter second no: </label> <input type="tel" maxlength="3" autofocus id="snum">
                </span> <br>

                <span style="display: none;" id="result">
                    addition is- <input type="number" disabled id="add"></input> <br>
                    subtraiction is- <input type="number" disabled id="sub"></input> <br>
                    multiplication is- <input type="number" disabled id="mul"></input> <br>
                    division is- <input type="number" disabled id="div" style="width: auto;"></input> <br>

                </span>

            </p>
        </div>

        <script>

            function mainFunction() {
                document.getElementById('run').style.display = 'block';
                document.getElementById("fnum").focus();
            }

            document.getElementById("fnum").addEventListener("keyup", function (e) {


                var sec = document.getElementById("sec");

                if (e.keyCode === 13) {
                    e.preventDefault();
                    var fnum = document.getElementById("fnum");
                    var snum = document.getElementById("snum");

                    sec.style.display = "block";
                    snum.focus();

                }
            });




            document.getElementById("snum").addEventListener("keyup", function (e) {

                var sec = document.getElementById("sec");
                var fnum = document.getElementById("fnum");
                var snum = document.getElementById("snum");
                var res = document.getElementById("result");
                var sub = document.getElementById("sub");
                var mul = document.getElementById("mul");
                var div = document.getElementById("div");

                if (e.keyCode === 13) {
                    e.preventDefault();

                    res.style.display = 'block';
                    snum.blur();

                    const sumnum = parseInt(fnum.value) + parseInt(snum.value);

                    document.getElementById("add").setAttribute("value", (sumnum));
                    document.getElementById("sub").setAttribute("value", (fnum.value - snum.value));
                    document.getElementById("mul").setAttribute("value", (fnum.value * snum.value));
                    document.getElementById("div").setAttribute("value", (fnum.value / snum.value));


                }
            });

        </script>







        <br> <br>
        <h3>2. WAP in C to find max number from two numbers using ternary operator. </h3>

        <pre>
    #include <span><</span>stdio.h>

        int main()
        {
        int num1, num2, max; 
     
        printf("Enter first numbers: ");
        scanf("%d", &num1);  
               
        printf("Enter second numbers: ");
        scanf("%d", &num2);
                        
        max = (num1 > num2) ? num1 : num2;   
          
        printf("Maximum between %d and %d is:  %d",num1, num2, max); 
        return 0;
                        
        }                                                                    
                </pre>









        <br> <br>
        <h3> 3. WAP in C to input student name and roll number and print Student name and roll number. (Hint : use
            scanf() for input and print() for output())</h3>
        <pre>


    #include <span><</span>stdio.h>

        int main()
        {
        char name; 
        int roll, branch;
              
        printf("please enter your information: \n");    
        
        printf("enter first charectar your name: "); 
        scanf("%c",&name); 
              
        printf("enter your roll number: "); 
        scanf("%d", &roll); 
          
        printf("enter your age: ");
        scanf("%d", &branch);
        
        printf("\n\ndisplay your all Information:\n"); 
              
        printf("your name is: %c\n", name); 
        printf("your roll number is: %d\n", roll); 
        printf("your branch is: %d", branch); 
        return 0;
         
        } 

</pre>











        <br> <br>
        <h3> 4. Write a program in C to generate a bell sound.</h3>
        <pre>

    #include <span><</span>stdio.h>

    int main()
    {     
        printf(" \a ");
        return 0;
    }
</pre>
        <br>
        <button class="btn btn-outline-success btn-block" onclick="bellFunction()">Run</button> <br>

        <p class="container-fluid bg-dark" style="display: none;" id="bellpera">output is a genrate bell: <br>
            <audio src="media/audio/sound.mp3" controls style="width: 0px;" id="sound"></audio>
        </p>


        <script>
            function bellFunction() {
                document.getElementById("bellpera").style.display = 'block';
                document.getElementById("sound").play();
            }
        </script>





        <br> <br>
        <h3> 5. WAP in C to print character of given ASCII value. </h3> <br>

        <pre>
    #include <span><</span>stdio.h>

        int main()
        {
        int ascii;
        
        printf("enter ascii value and find char: ");
        scanf("%d",&ascii);
        
        char name = ascii;
        printf("char is %c", name);
        
        return 0;
         
        }
</pre>









        <br> <br>
        <h3> 6. WAP in C to find square of given number. </h3> <br>

        <pre>

    #include <span><</span>stdio.h>

        int main()
        {
        int num, sqr;
        
        printf("enter number and find squre: ");
        scanf("%d",&num);
            
        sqr = num*num;
            
        printf("squre number is: %d", sqr);
            
        return 0;
            
        } 

</pre>
        <button class="btn btn-outline-success btn-block" onclick="sqrfunction()">Run</button> <br>

        <div class="container-fluid bg-dark" style="display: none;" id="bellperagraph">

            <p> enter number and find squre: <input type="tel" maxlength="3" id="sqrnum"> <br>
                <span style="display: none;" id="span_res_pergrapg"> squre number is: <span id="sqr_result"
                        style="color: aliceblue;"></span> </span> </p>

        </div>


        <script>
            function sqrfunction() {
                document.getElementById("bellperagraph").style.display = 'block';
                document.getElementById("sqrnum").focus();
            }

            document.getElementById("sqrnum").addEventListener("keyup", function (e) {
                if (e.keyCode === 13) {
                    e.preventDefault();

                    document.getElementById("span_res_pergrapg").style.display = 'block';
                    var sqr_num_sqr = document.getElementById("sqrnum");
                    sqr_num_sqr.blur();

                    document.getElementById("sqr_result").innerHTML = sqr_num_sqr.value * sqr_num_sqr.value;

                }
            });
        </script>







        <br> <br>
        <h3>7. WAP in C to calculate average of three numbers. </h3>

        <pre>

    #include <span><</span>stdio.h>
        int main()
        {
        int a,b,c;
        float avg;
        printf("\tEnter Three Numbers\n");
            
        printf("Enter First Number  : ");
        scanf("%d", &a);
        
        printf("\nEnter Second Number : ");
        scanf("%d",&b);
        
        printf("\nEnter Third Number : ");
        scanf("%d",&c);
        
        avg = (a+b+c) / 3.0;
        printf("\nAverage of Three Numbers : %f",avg);
        
        return 0;
        }   
                                                                        
</pre>




        <br> <br>
        <h3>9. WAP in C to convert temperature in Celsius from Fahrenheit. (Hint : C= (F – 32 ) x 5/9)</h3>

        <pre>


#include<span><</span>stdio.h>

    int main()
    {
        float celsius, fahrenheit;
    
        printf("enter temperature in Fahrenheit: ");
        scanf("%f", &fahrenheit);
    
        celsius = (fahrenheit - 32) * 5 / 9;
    
        printf("%f Fahrenheit = %f Celsius", fahrenheit, celsius);
    
        return 0;
    }
                                                                        
</pre>






        <br> <br>
        <h3> 11. WAP in C to print ASCII value of given character. </h3> <br>

        <pre>
    #include <span><</span>stdio.h>

        int main()
        {
        char name;
            
        printf("enter char value and find ascii: ");
        scanf("%c",&name);
            
        int ascii = name;
        printf("char is %d", ascii);
        return 0;
            
        }

</pre>


        <button class="btn  d-block m-auto "> <a href="source/a1.txt" download="Assignment 1st"> Download this
                Assignment </a> </button> <br> <br>

        <a href="a2.py" class="float-right"> next <i class="fa fa-angle-double-right "></i> </a>

        <br> <br> <br> <br>


    </div>

</body>

</html>

""")
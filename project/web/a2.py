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

    <title>Assignment Two</title>
    <script src="js/main.js"></script>
    <link rel="shortcut icon" href="../media/image/logo.svg" type="image/x-icon">
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
                <a class="nav-link active disabled"> <b>Assignment 2.</b> </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down" download="assignmebt 2" href="source/a2.txt"> Download </a>
            </li>

        </ul>
    </nav>



    <div class="container"> <br>



        <h3>1. Write a program in c to find greatest number between three numbers. </h3>

        <pre>
            #include<span><</span>stdio.h>
            #include<span><</span>conio.h>
                 
                int main()
                {
                    int num1, num2, num3;
                 
                    printf("enter first no: ", num1);
                    scanf("%d", &num1);
                
                    printf("enter second no: ", num2);
                    scanf("%d", &num2);
                
                    printf("enter third no: ", num3);
                    scanf("%d", &num3);
                
                
                    if (num1 > num2)
                    {
                        if (num1 > num3)
                        {
                            printf("%d is greatest num.", num1);
                        }
                        else
                        {
                           printf("%d is greatest num.", num3);
                        }
                    }
                    else if (num2 > num3)
                        printf("%d is greatest num.", num2);
                    else
                        printf("%d is greatest num.", num3);
                
                        return 0;
                }
        </pre>

        <button class="btn btn-outline-success btn-block" onclick="mainFunction()">Run</button> <br>

        <div class="container-fluid bg-dark">

            <p style="display: none;" id="run">
                <label for="fnum">enter first no:</label> <input type="tel" autofocus maxlength="3" id="fnum"> <br>

                <span style="display: none;" id="sec">
                    <label for="snum"> enter second no: </label> <input type="tel" maxlength="3" autofocus id="snum">
                </span>

                <span style="display: none;" id="third">
                    <label for="snum"> enter third no: </label> <input type="tel" maxlength="3" autofocus id="tnum">
                </span>

                <span style="display: none;" id="result">

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


            document.getElementById("fnum").addEventListener("keyup", function (e) {


                var sec = document.getElementById("sec");

                if (e.keyCode === 13) {
                    e.preventDefault();

                    sec.style.display = "block";
                    snum.focus();

                }
            });


            document.getElementById("snum").addEventListener("keyup", function (e) {


                var third = document.getElementById("third");

                if (e.keyCode === 13) {
                    e.preventDefault();

                    third.style.display = "block";
                    tnum.focus();

                }
            });


            document.getElementById("tnum").addEventListener("keyup", function (e) {


                var result = document.getElementById("result");

                if (e.keyCode === 13) {
                    e.preventDefault();

                    result.style.display = "block";
                    tnum.blur();

                    var fnum = document.getElementById("fnum");
                    var snum = document.getElementById("snum");
                    var tnum = document.getElementById("tnum");
                    const greatestNum;

                    if (fnum > snum) {
                        if (fnum > tnum) {
                            greatestNum = fnum.value;
                        } else {
                            greatestNum = tnum.value;
                        }
                    } else if (snum > tnum) {
                        greatestNum = snum.value;
                    } else {
                        greatestNum = tnum.value;
                    }

                    result.innerHTML = greatestNum + " is greatest number.";

                }
            });




        </script>







        <h3>2. Write a program in c to find odd & even number. </h3>

        <pre>

        #include <span><</span>stdio.h>
            int main() {
                int num;
                printf("enter integer no: ");
                scanf("%d", &num);
            
                if(num % 2 == 0) {
                    printf("%d is even.", num);
                } else {
                    printf("%d is odd.", num);
                }
                
                return 0;
            }

     </pre>




        <h3>3. Write a program in c to check entered number is positive or negative. </h3>

        <pre>

        #include <span><</span>stdio.h>
 
            void main()
            {
                int number;
             
                printf("enter a no: ");
                scanf("%d", &number);

                if (number >= 0) {
                    printf("%d is a positive number \n", number);
                 } else {
                    printf("%d is a negative number \n", number);
                 }
            }

    </pre>



        <h3>4. Write a program in c to enter year and check input year is leap year or not. </h3>

        <pre>

    #include <span><</span>stdio.h>

        int main()
        {
            int year;
        
            printf("enter year : ");
            scanf("%d", &year);
        
        
            if(year % 4 == 0)
            {
                printf("leap year");
            }
            else
            {
                printf("genral year");
            }
        
            return 0;
        }

     </pre>



        <h3>5. Write a program in c to check that give character is vowel or consonant.</h3>

        <pre>

        #include <span><</span>stdio.h>

            int main()
            {
                char chr;
            
                printf("enter char: ");
                scanf("%c", &chr);
            
            
                if(chr == 'a' || chr == 'A' || chr == 'e' || 
                   chr == 'E' || chr == 'i' || chr == 'I' || 
                   chr == 'o' || chr == 'O' || chr == 'u' || chr == 'U' )
                {
                    printf("char is vovel.");
                }
                else
                {
                    printf("char is consonant");
                }
            
                return 0;
            }

     </pre> <br><br>




        <h3>6. Write a program in c to input a character and check character is in uppercase or in lowercase.</h3>

        <pre>

        #include<span><</span>stdio.h>
 
    int main() {
       char chr;
     
       printf("\nEnter The Character : ");
       scanf("%c", &chr);
     
       if (chr >= 'A' && chr <= 'Z')
          printf("Character is Upper Case ");
       else
          printf("Character is  Lower Case ");
     
       return (0);
    }

     </pre>


        <h3>7. Write a program in c to find greatest number between four number using ternary operator. </h3>

        <pre>

#include <span><</span>stdio.h> 

  int main() 
  { 
      int n1, n2, n3, n4, max; 

       printf("enter 1st no: ");
       scanf("%d",&n1);

       printf("enter 2nd no: ");
       scanf("%d",&n2);

       printf("enter 3rd no: ");
       scanf("%d",&n3);

       printf("enter 4th no: ");
       scanf("%d",&n4);
        
      max = (n1 > n2 && n1 > n3 && n1 > n4) ?  
                                     n1 :  
                                       ((n2 > n3 && n2 > n4) ?  
                                                           n2 :  
                                                            (n3 > n4 ? n3 : n4)); 
        
      printf("Largest number is %d.", max); 
    
      return 0; 
  }
   </pre>

        <h3>9. Write a program in C to print week day according to day number.</h3>

        <pre>

        #include<span><</span>stdio.h>
     
            int main()
                {
                   
                    int day;
        
                    printf("enter day no: ");
                    scanf("%d",&day);
                   
                    
                    switch (day)
                    {
                    case 1:
                        printf("Monday");
                        break;
        
                    case 2:
                        printf("Tuesday");
                        break;
        
                    case 3:
                        printf("Wednesday");
                        break;
        
                     case 4:
                        printf("Thirsday");
                        break;
        
                    case 5:
                        printf("Friday");
                        break;
        
                    case 6:
                        printf("Sturday");
                        break;
        
                    case 7:
                        printf("Sunday");
                        break;
                    
                    default:
                        printf("Defaul day no.");
                        break;
                    }
                
                        return 0;
                }        

     </pre>



        <h3>10. Write a program in c to calculate mathematical operations using switch case.</h3>

        <pre>

    #include<span><</span>stdio.h>
    #include<span><</span>conio.h>
         
    int main()
        {
           
            int num1, add, mul, sub;
            char oprator;
            float num2, div;

            printf("enter oprator: ",oprator);
            scanf("%c",&oprator);
           
            printf("enter first no: ");
            scanf("%d",&num1);

            printf("enter second no: ");
            scanf("%f", &num2); 

            add = num1 + num2;
            sub = num1 - num2;
            mul = num1 * num2;
            div = num1 / num2;

            switch (oprator)
            {
            case '+':
                printf("addition is: %d", add);
                break;

            case '-':
                printf("subtretion is: %d", sub);
                break;

            case '*':
                printf("multiplication is: %d", mul);
                break;

            case '/':
                printf("division is: %f", div);
                break;
            
            default:
                printf("default oprator.");
                break;
            }
        
                return 0;
        }

  </pre>


        <button class="btn  d-block m-auto "> <a href="source/a2.txt" download="Assignment 2nd"> Download this
                Assignment </a> </button> <br> <br>
        <a href="a1.py"> <i class="fa fa-angle-double-left float-left"> privious </i> </a>
        <a href="a3.py" class="float-right"> next <i class="fa fa-angle-double-right "> </i> </a>
        <br> <br> <br> <br>
    </div>

</body>

</html>

""")
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

    <title>Assignment Three</title>
    <link rel="shortcut icon" href="../media/image/logo.svg" type="image/x-icon">
    <script src="js/main.js"></script>
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
                <a class="nav-link active disabled"> <b>Assignment 3.</b> </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down" download="assignmebt 3" href="source/a3.txt"> Download </a>
            </li>

        </ul>
    </nav>


    <div class="container"> <br>

        <h3>1. Write a program in c generate Fibonacci series up to given number.</h3>

        <pre>

            #include <span><</span>stdio.h>
                int main() {
                    int i, n, t1 = 0, t2 = 1, nextTerm;
                    printf("Enter the number of terms: ");
                    scanf("%d", &n);
                    printf("Fibonacci Series: ");
                
                    for (i = 1; i <= n; ++i) {
                        printf("%d, ", t1);
                        nextTerm = t1 + t2;
                        t1 = t2;
                        t2 = nextTerm;
                    }
                
                    return 0;
                }
        </pre>




        <h3>2. Write a program in c to reverse the digit of a given number.</h3>

        <pre>

        #include <span><</span>stdio.h>
        #include <span><</span>string.h>
            int main()
            {
               char s[10];
            
               printf("enter a number to reverse: ");
               gets(s);
            
               strrev(s);
            
               printf("reverse no is: %s\n", s);
            
               return 0;
            }  

     </pre>



        <h3>3. Write a program in c to make a table of a given number.</h3>

        <pre>

        #include <span><</span>stdio.h>
        int main()
        {
            int num, result;

            printf("enter no: ");
            scanf("%d", &num);

            for(int i = 1; i <= 10; i++){
                result = num * i;
                printf("%d * %d = %d \n",num, i, result);
            }

            return 0;
        }
 
     </pre>


        <h3>4. Write a program in c to find the factorial of given number. </h3>

        <pre>

    #include <span><</span>stdio.h>
 
    int main() {
    int n, fact = 1;
    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("negative number doesn't exist.");
     } else {
        for (int i = 1; i <= n; ++i) {
            fact *= i;
        }
        printf("factorial of %d is = %d", n, fact);
    }

    return 0;
    }

    </pre>



        <h3>5. Write a program in c to sum of digits of a given number.</h3>

        <pre>

    #include <span><</span>stdio.h>

        int main()
        {
            int num, sum=0;
        
            printf("enter number: ");
            scanf("%d", &num);
        
            while(num!=0)
            {
                sum += num % 10;
                num = num / 10;
            }
        
            printf("sum of digits = %d", sum);
        
            return 0;
        }

     </pre>



        <h3>9. Write a program in c to print all alphabet from a to z.</h3>

        <pre>

        #include <span><</span>stdio.h>

        int main()
        {
            char ch;
        
            printf("prints alphabets: \n");
            for(ch='a'; ch<='z'; ch++)
            {
                printf("%c\n", ch);
            }
        
            return 0;
        }

     </pre> <br><br>




        <h3>10. WAP in C to print Even number up to given number.</h3>

        <pre>

        #include<span><</span>stdio.h>
        void main()
        {
             int i,n;
        
             printf("enter number: ");
             scanf(" %d",&n);
        
             printf("even numbers up to inputted number are - ");
        
             for(i=2;i<=n;i+=2)
             {
                     printf(" %d \n",i);
             }
        } 

     </pre>

        <button class="btn  d-block m-auto "> <a href="source/a3.txt" download="Assignment 3rd"> Download this
                Assignment </a> </button> <br> <br>

        <a href="a2.py"> <i class="fa fa-angle-double-left float-left"> privious </i> </a>
        <a href="a4.py" class="float-right"> next <i class="fa fa-angle-double-right "> </i> </a>
        <br> <br> <br> <br>
    </div>

</body>

</html>

""")
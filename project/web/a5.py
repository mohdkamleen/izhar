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

    <title>Assignment five</title>
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
                <a class="nav-link active disabled"> <b> Assignment 5.</b> </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="project.py"> Project's </a>
            </li>

            <li class="nav-item">
                <a class="nav-link fa fa-angle-double-down float-left" download="assignmebt 5" href="source/a5.txt">
                    Download </a>
            </li>

        </ul>
    </nav>


    <div class="container"> <br>
        <h3>1. WAP in c to input two matrix and perform addition of matrix.</h3>

        <pre>

        #include <span><</span>stdio.h>
            int main() {
                int r, c, a[100][100], b[100][100], sum[100][100], i, j;
                printf("Enter the number of rows (between 1 and 100): ");
                scanf("%d", &r);
                printf("Enter the number of columns (between 1 and 100): ");
                scanf("%d", &c);
            
                printf("\nEnter elements of 1st matrix:\n");
                for (i = 0; i < r; ++i)
                    for (j = 0; j < c; ++j) {
                        printf("Enter element a%d%d: ", i + 1, j + 1);
                        scanf("%d", &a[i][j]);
                    }
            
                printf("Enter elements of 2nd matrix:\n");
                for (i = 0; i < r; ++i)
                    for (j = 0; j < c; ++j) {
                        printf("Enter element a%d%d: ", i + 1, j + 1);
                        scanf("%d", &b[i][j]);
                    }
            
                // adding two matrices
                for (i = 0; i < r; ++i)
                    for (j = 0; j < c; ++j) {
                        sum[i][j] = a[i][j] + b[i][j];
                    }
            
                // printing the result
                printf("\nSum of two matrices: \n");
                for (i = 0; i < r; ++i)
                    for (j = 0; j < c; ++j) {
                        printf("%d   ", sum[i][j]);
                        if (j == c - 1) {
                            printf("\n\n");
                        }
                    }
            
                return 0;
            }         
            
            
       </pre>

        <h3>2. WAP in c to input two matrix and perform subtraction of matrix.</h3>
        <pre>

        #include <span><</span>stdio.h>
 
            int main()
            {
               int m, n, c, d, first[10][10], second[10][10], difference[10][10];
             
               printf("Enter the number of rows and columns of matrix\n");
               scanf("%d%d", &m, &n);
               printf("Enter the elements of first matrix\n");
             
               for (c = 0; c < m; c++)
                 for (d = 0 ; d < n; d++)
                   scanf("%d", &first[c][d]);
             
               printf("Enter the elements of second matrix\n");
             
               for (c = 0; c < m; c++)
                 for (d = 0; d < n; d++)
                     scanf("%d", &second[c][d]);
             
               printf("Difference of entered matrices:-\n");
             
               for (c = 0; c < m; c++) {
                 for (d = 0; d < n; d++) {
                   difference[c][d] = first[c][d] - second[c][d];
                   printf("%d\t",difference[c][d]);
                 }
                 printf("\n");
               }
             
               return 0;
            }


       </pre>

        <h3>3. WAP in c to input two matrix and perform multiplication of </h3>
        <pre>

        #include <span><</span>stdio.h>

            void enterData(int firstMatrix[][10], int secondMatrix[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond);
            void multiplyMatrices(int firstMatrix[][10], int secondMatrix[][10], int multResult[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond);
            void display(int mult[][10], int rowFirst, int columnSecond);
            
            int main()
            {
                int firstMatrix[10][10], secondMatrix[10][10], mult[10][10], rowFirst, columnFirst, rowSecond, columnSecond, i, j, k;
            
                printf("Enter rows and column for first matrix: ");
                scanf("%d %d", &rowFirst, &columnFirst);
            
                printf("Enter rows and column for second matrix: ");
                scanf("%d %d", &rowSecond, &columnSecond);
            
                // If colum of first matrix in not equal to row of second matrix, asking user to enter the size of matrix again.
                while (columnFirst != rowSecond)
                {
                    printf("Error! column of first matrix not equal to row of second.\n");
                    printf("Enter rows and column for first matrix: ");
                    scanf("%d%d", &rowFirst, &columnFirst);
                    printf("Enter rows and column for second matrix: ");
                    scanf("%d%d", &rowSecond, &columnSecond);
                }
            
                // Function to take matrices data
                    enterData(firstMatrix, secondMatrix, rowFirst, columnFirst, rowSecond, columnSecond);
            
                    // Function to multiply two matrices.
                    multiplyMatrices(firstMatrix, secondMatrix, mult, rowFirst, columnFirst, rowSecond, columnSecond);
            
                    // Function to display resultant matrix after multiplication.
                    display(mult, rowFirst, columnSecond);
            
                return 0;
            }
            
            void enterData(int firstMatrix[][10], int secondMatrix[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond)
            {
                int i, j;
                printf("\nEnter elements of matrix 1:\n");
                for(i = 0; i < rowFirst; ++i)
                {
                    for(j = 0; j < columnFirst; ++j)
                    {
                        printf("Enter elements a%d%d: ", i + 1, j + 1);
                        scanf("%d", &firstMatrix[i][j]);
                    }
                }
            
                printf("\nEnter elements of matrix 2:\n");
                for(i = 0; i < rowSecond; ++i)
                {
                    for(j = 0; j < columnSecond; ++j)
                    {
                        printf("Enter elements b%d%d: ", i + 1, j + 1);
                        scanf("%d", &secondMatrix[i][j]);
                    }
                }
            }
            
            void multiplyMatrices(int firstMatrix[][10], int secondMatrix[][10], int mult[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond)
            {
                int i, j, k;
            
                // Initializing elements of matrix mult to 0.
                for(i = 0; i < rowFirst; ++i)
                {
                    for(j = 0; j < columnSecond; ++j)
                    {
                        mult[i][j] = 0;
                    }
                }
            
                // Multiplying matrix firstMatrix and secondMatrix and storing in array mult.
                for(i = 0; i < rowFirst; ++i)
                {
                    for(j = 0; j < columnSecond; ++j)
                    {
                        for(k=0; k<span><</span>columnFirst; ++k)
                        {
                            mult[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
                        }
                    }
                }
            }
            
            void display(int mult[][10], int rowFirst, int columnSecond)
            {
                int i, j;
                printf("\nOutput Matrix:\n");
                for(i = 0; i < rowFirst; ++i)
                {
                    for(j = 0; j < columnSecond; ++j)
                    {
                        printf("%d  ", mult[i][j]);
                        if(j == columnSecond - 1)
                            printf("\n\n");
                    }
                }
            } 

       </pre> <br>

        <button class="btn  d-block m-auto "> <a href="source/a5.txt" download="Assignment 5th"> Download this
                Assignment </a> </button> <br> <br>


        <a href="a4.py"> <i class="fa fa-angle-double-left float-left"> privious </i> </a> <br> <br> <br>
    </div>

</body>

</html>

""")
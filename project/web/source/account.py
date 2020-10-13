#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\r\n\r\n")

print("""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="rgb(214, 218, 215)">
    <meta name="Keywords"
        content="HTML,CSS,JavaScript,SQL,PHP,jQuery,Bootstrap,Python,C,C++,digicoders,training,summer training">
    <meta name="Description"
        content=" In this Website Im trained with digicoders and its makeing for my all Projet, Assignment and about me and my training company....... ">
    <meta property="og:logo"
        content="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <meta property="og:url" content="https://mohdkamleen.github.io/digicoders/">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Plink - Create payment links and send them to your clients">
    <meta property="og:description" content="Im trained with digicoders and its makeing for my all Projet.">
    <meta property="og:image"
        content="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <meta property="og:site_name" content="digicoders">
    <meta property="og:locale" content="en-EN">
    <meta property="og:locale:alternate" content="nl-NL">
    <meta property="og:locale:alternate" content="de-DE">
    <meta property="og:locale:alternate" content="fr-FR">
    <meta name='robots' content='index,follow' />
    <meta name="msapplication-TileColor" content="rgb(214, 218, 215)">
    <link rel="apple-touch-icon"
        href="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <title> User's Home Page </title>
    <!-- title image favicon  -->
    <link rel="shortcut icon" href="../media/image/logo.svg" type="image/x-icon">
    <!-- manually style sheet  -->
    <link rel="stylesheet" href="../css/loader.css">
    <link rel="stylesheet" href="../css/nav.css">
    <link rel="stylesheet" href="../css/user.css">
    <link rel="stylesheet" href="../css/main.css"> 
    <link rel="stylesheet" href="../css/bootstraph.css"> 
    <!-- dark mode access style sheet  -->
    <link rel="stylesheet" href="../css/dark.css">
    <link rel="stylesheet" id="style">

</head>



<body id="cssChange">
    <div id="main_div">

        <div class="header">

            <!-- preloader  -->
            <div class="preloader">
                <span><b>0</b>%</span>
                <p>Loading<b>.</b><b>.</b><b>.</b></p>
            </div> 

            <!-- navigation seceion  -->
            <nav>
                <div class="navigation">
                    <div class="logo">
                        <h1>kam<span>leen</span></h1>
                    </div>

                    <div class="navbar">
                        <ul>
                            <li><a href="../index.py">Home </a></li>
                            <li><a href="../project.py">Project</a></li>
                            <li><a href="../contact.py">Contact</a></li>
                            <li><a href="../other.py">Other</a></li>
                        </ul>
                    </div>
                    <div class="hamburger"></div>
                </div>
                <div class="menu_background1"></div>
                <div class="menu_background2"></div>
            </nav>
            <header>
                <section>
                    <div class="body_content_header">
                        <div class="nav_background"></div>
                        <div class="nav_hamburger_background"></div>

                        <div class="header_top">
                            <div class="about-me">
                                <h3> <span style="font-size: 1.7rem;">Congratulations!!!!!!! </span> <br> 
                                    you are available to my website. <br><br>
                                    Authentication is the process of determining if the request has come from a valid
                                    user who has the required privileges to use the system. In the world of computer
                                    networking this is a very vital requirement as many systems keep interacting with
                                    each other and proper mechanism needs to ensure that only valid interactions happen
                                    between these programs.
                                    <br><br>  
                                </h3>
                            </div>
                            <div class="header_img">
                                <img class="nav_background_img" src="../media/image/undraw_smart_home_28oy.svg"
                                    alt="header image">
                            </div>
                        </div>

                    </div>

        <div class="show_user">
          
 
   
        </div>
                </section>
            </header> 
        </div>
    </div>


    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="../js/main.js"></script>
    <script src="../js/nav.js"></script>
    <script>

    document.getElementById("cssChange").onclick = () => { 

    let arr = [
        "", "../css/change/blue.css",
        "", "../css/change/blue2.css",
        "", "../css/change/blue3.css",
        "", "../css/change/red.css",
        "", "../css/change/red2.css",
        "", "../css/change/red3.css",
        "", "../css/change/green.css",
        "", "../css/change/green2.css",
        "", "../css/change/yellow.css",
        "", "../css/change/yellow2.css",
        "", "../css/change/gray.css",
        "", "../css/change/gray2.css",
        "", "../css/change/pink.css",
        "", "../css/change/cyan.css",
        "", "../css/change/cyan2.css",
        "", "../css/change/red.css"
    ]
  
   let styleSheet = arr[Math.floor(Math.random() * arr.length)];
   style.setAttribute("href", styleSheet);


}  
    </script>
</body>

</html>

""")
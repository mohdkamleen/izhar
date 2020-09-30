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
    <title>Mohd Kamleen</title>
    <!-- title image favicon  -->
    <link rel="shortcut icon" href="media/image/logo.svg" type="image/x-icon"> 
    <!-- manually style sheet  -->
    <link rel="stylesheet" href="css/nav.css">
    <link rel="stylesheet" href="css/home-body.css">
    <link rel="stylesheet" href="css/home-header.css">
    <link rel="stylesheet" href="css/loader.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" id="style">
    <!-- dark mode access style sheet  -->
    <link rel="stylesheet" href="css/dark.css">


</head>

<body>

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
                            <li><a class="active"> Home </a></li>
                            <li><a href="project.py">Project</a></li>
                            <li><a href="contact.py">Contact</a></li>
                            <li><a href="other.py">Other</a></li>
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
                        <a href="#trigger" class="trigger-target">
                            <div class="scroll_down"></div>
                        </a>
                        <div class="nav_hamburger_background"></div>

                        <div class="header_top">
                            <div class="header_text">
                                <div class="text">
                                    <span>hey!!!!</span>
                                    <hr>
                                    <h2>I'm <span class="type_text"></span></h2>
                                </div>
                                <div class="btn-group">
                                    <button class="btn "> <a download="kamleen's resume" href="https://mohdkamleen.github.io/digicoders/image/resume.png">Download CV</a></button>
                                    <button class="btn "><a href="mailto:kamleenmohd@gmail.com"> Hire Me</a></button>
                                </div>
                            </div>
                            <div class="header_img">
                                <img class="nav_background_img" src="media/image/undraw_web_developer_p3e5.svg"
                                    alt="header image">
                            </div>
                        </div>

                    </div>
                </section>
            </header>

        </div>

        <div class="main_container">

            <div class="container" id="trigger">
                <h4>
                 <b>About me</b> <br>
                    My name is Mohd Kamleen. I'm 19years old. Currently, I am living in Ambedkar Nagar, India. I am
                    working as a student at CSJM GOVT POLY Ambedkar Nagar. And I am a student and weavers. And I learn
                    programming language with digicoders. Click here to check my CV.
                </h4>

                <div class="img">
                    <img src="media/image/kamleen.png" alt="">
                </div>

            </div>

            <div class="container2">
                <div class="img">
                    <img src="media/image/undraw_best_place_r685.svg"
                        alt="">
                </div>
                <h4>
                    <b>DigiCoders Technologies</b> <br>
                    &nbsp; &nbsp; &nbsp;  This is the best Software Development Company in Lucknow. He Leading by young software Engineers and
                    Entrepreneurs. Software Company today operates on many different business model and provide a wide
                    array
                    of products and services. A software Company to become faster and more productive for the customer
                    than
                    ever. DigiCoders Technologies Best software development company in Lucknow. At DigiCoders he have
                    world's top developer of enterprise solution commonly known as an infrastructure as a services
                    (IaaS)
                    with SaaS powering many IaaS solutions. We Provide the best Software services like Software
                    development
                    Website Development, Mobile Application Development, Digital Marketing, and Training Programs.
                </h4>
            </div>
        </div>

    </div>


    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.11"></script>
    <script src="js/nav.js"></script>
    <script src="js/main.js"></script>
    <script src="js/type.js"></script> 
    <script>
        $(document).ready(function () {
            $(".trigger-target").on('click', function (event) {
                if (this.hash !== "") {
                    event.preventDefault();

                    var hash = this.hash;

                    $('html, body').animate({
                        scrollTop: $(hash).offset().top
                    }, 800, function () {
                        window.location.hash = hash;
                    });
                }
            });
        });
    </script>
 

</body>

</html>

""")
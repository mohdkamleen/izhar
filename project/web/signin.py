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
	<title>Mohd Kamleen | SignIn </title>
	<!-- title image favicon  -->
	<link rel="shortcut icon" href="media/image/logo.svg" type="image/x-icon">
	<!-- manually style sheet  -->
	<link rel="stylesheet" href="css/contact.css">
	<link rel="stylesheet" href="css/loader.css">
	<link rel="stylesheet" href="css/nav.css">
	<link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" id="style" >
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
							<li><a href="index.py">Home </a></li>
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
						<div class="nav_hamburger_background"></div>

						<div class="header_top">
							<h3 style="padding: 10px 5%;">
								SignIn Form Here! <br><br>
								Need to login for an account <br>
								<button class="btn"> <a href="login.py">Login</a></button>
							</h3>

							<div class="header_img">
								<img class="nav_background_img" src="media/image/undraw_Access_account_re_8spm.svg"
									alt="header image">
							</div>
						</div>

					</div>
				</section>
			</header>

		</div> 

	<div class="container2">
		<span class="big-circle"></span>
		<img src="img/shape.png" class="square" alt="" />
		<div class="form">
			<div class="contact-info">
				<h3 class="title">Let's get in Sign Up</h3>
				<p class="text">
					You are more than welcome to signin for demo using this form. * indicates required field.
					Name:*. Email:*. .phone:*. . Password:*. 
				</p>

				<div class="info">
					<div class="information">
						<img src="media/image/undraw_Access_account_re_8spm.svg" class="icon" alt="" />
						<p> It's sign up only for demo</p>
					</div>
					<div class="information">
						<img src="media/image/undraw_secure_login_pdn4.svg" class="icon" alt="" />
						<p>Using Google Chrome? Get Login for Chrome!</p>
					</div>
					<div class="information">
						<img src="media/image/undraw_smart_home_28oy.svg" class="icon" alt="" />
						<p>Need to sign up for an account or reset your password?</p>
					</div>
				</div>

				<div class="social-media">
					<p>SignIn with us :</p>
					<div class="social-icons">
						<a href="404.html">
							<i class="fab fa-facebook-f"></i>
						</a>
						<a href="404.html">
							<i class="fab fa-twitter"></i>
						</a>
						<a href="404.html">
							<i class="fab fa-instagram"></i>
						</a>
						<a href="404.html">
							<i class="fab fa-linkedin-in"></i>
						</a>
					</div>
				</div>
			</div>

			<div class="contact-form2">
				<span class="circle one"></span>
				<span class="circle two"></span>

				<form action="action/signin.py" method="POST">
					<h3 class="title">SignIn</h3>
					<div class="input-container">
						<input required type="text" name="name" class="input" />
						<label for="">Name</label>
						<span>Name</span>
					</div>
					<div class="input-container">
						<input required type="email" name="email" class="input" />
						<label for="">Email</label>
						<span>Email</span>
					</div> 
					<input type="hidden" name="date" id="comment_datetime">
					<div class="input-container">
						<input autocomplete="off" required type="password" name="password" class="input" />
						<label for="">Password</label>
						<span>Password</span> 
					</div>   
					<input type="submit" value="Send" class="btn" />
				</form>
			</div>
		</div>
	</div>






	</div>

	<script src="https://kit.fontawesome.com/64d58efce2.js" crossorigin="anonymous"></script>

	<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
	<script src="js/main.js"></script>
	<script src="js/nav.js"></script>
	<script src="js/time.js"></script>
	<script src="js/contact.js"></script> 

</body>

</html>

""")
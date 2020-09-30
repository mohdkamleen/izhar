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

  <title>Task 8 | html </title>
  <link rel="stylesheet" href="css/bootstraph.css">
    <script src="js/main.js"></script>
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

    .form-group {
      border: 2px solid gray;
      padding: 20px;
    }

    p {
      font-size: 20px;
      color: green;
      padding: 10px;
    }

    h1 {
      color: #555555;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: lighter;
    }

    #result_show {
      position: fixed;
      top: 30%;
      left: 30%;
      background: transparent;
      border: 2px solid gray;
      padding: 20px;
      border-radius: 5px;
      transition: all .3s ease-in;
      transform: scale(0);
      z-index: 1;
    }

    .form-control:focus {
      box-shadow: 1px 1px 5px 1px rgb(152, 152, 167),
        1px -1px 7px 2px rgb(100, 100, 102);
      border: 2px solid gray;
    }

    .form-control {
      border: 2px solid gray;
    }

    .container {
      max-width: 400px;
    }
  </style>
</head>

<body class="animate__animated animate__zoomIn">

  <!-- nav section  -->

  <div id="fluid">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
      <!-- Brand -->
      <a class="navbar-brand animate__pulse animate__animated animate__infinite" href="#">Html</a>

      <!-- Links -->
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <a class="nav-link active disabled"> <b> Task 8.</b> </a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="project.py"> Project's </a>
        </li>

        <li class="nav-item">
          <a class="nav-link fa fa-angle-double-down float-left" download="task 8" href="t8.py"> Download </a>
        </li>

      </ul>
    </nav>

    <div class="container-fluid">
      <br>
      <h1>1. Design a calculator like this.</h1>

      <div class="form-group container">
        <h3 class="text-center">calculator</h3> <br>
        <input onkeyup="check_num1()" placeholder="Enter first number maximum 5" class="form-control"> <br>
        <input onkeyup="check_num2()" placeholder="Enter second number maximum 4" class="form-control"> <br>
        <input type="button" onclick="result()" disabled value="Result" class="d-block m-auto" id="result_button"> <br>
      </div>


      <br> <br>
      <h1>2. Design a calculator like this pattern.</h1>
      <object data="source/t8.2.py" style=" height: 700px; width: 100%;"></object> <br> <br> <br>
    </div>

  </div>
  <script>
    function result() {
      document.getElementById('result_show').style.transform = 'scale(1)';
      document.getElementById('fluid').style.filter = 'blur(3px)'
      var num1 = document.getElementsByClassName('form-control')[0].value;
      var num2 = document.getElementsByClassName('form-control')[1].value;
      var num1 = parseInt(num1);
      var num2 = parseInt(num2);
      var add = num1 + num2;
      var sub = num1 - num2;
      var mul = num1 * num2;
      var div = num1 / num2;
      var mod = num1 % num2;
      document.getElementById('main_result').innerHTML = "Addition = " + add + '<br>' + "Subtraction = " + sub + '<br>' + "Multiplication = " + mul + '<br>' + "Division = " + div + '<br>' + "modulo = " + mod;
    }

    function hide() {
      document.getElementById('result_show').style.transform = 'scale(0)';
      document.getElementById('fluid').style.filter = 'blur(0px)'
    }

    function check_num1() {
      var n1 = document.getElementsByClassName('form-control')[0];
      var number_check = /^[0-9]{1,5}$/;
      if (number_check.test(n1.value)) {
        document.getElementById('result_button').disabled = false;
        n1.style.color = 'gray';
        n1.style.borderColor = 'gray';
      } else {
        document.getElementById('result_button').disabled = true;
        n1.style.color = 'red';
        n1.style.borderColor = 'red';
      }
    }

    function check_num2() {
      var n2 = document.getElementsByClassName('form-control')[1];
      var number2_check = /^[0-9]{1,4}$/;
      if (number2_check.test(n2.value)) {
        document.getElementById('result_button').disabled = false;
        n2.style.color = 'gray';
        n2.style.borderColor = 'gray';
      } else {
        document.getElementById('result_button').disabled = true;
        n2.style.color = 'red';
        n2.style.borderColor = 'red';
      }
    }


  </script>

  <div id="result_show">
    <h2 class="text-center text-dark p-2">Results</h2>
    <h4 id="main_result" class="text-secondary "></h4>
    <button class="btn btn-outline-secondary" onclick="hide()">cancel</button>
  </div>


</body>

</html>

""")
let preloader = document.querySelector("div.preloader"); 
let preloader_counter = document.querySelector("div.preloader span b"); 
let nav_hamberger_background = document.querySelector(".nav_hamburger_background");  
let nav_background = document.querySelector(".nav_background"); 
let scroll_down = document.querySelector(" .scroll_down");  
let style = document.getElementById("style"); 
let mousemove = document.getElementById("mousemove");

window.onload = () => {
    preloader.classList.add("active"); 
    nav_background.classList.add("show"); 
}  
 

window.onscroll = () => {
    let windowPageYOffset = window.pageYOffset;
    if(windowPageYOffset > 400){
        nav_hamberger_background.classList.add("show"); 
    } else {
        nav_hamberger_background.classList.remove("show");
    }

    if(windowPageYOffset > 0){
        // scroll_down.style.transform = "translateY(-10px)";
        scroll_down.style.opacity = "0"; 
    } else {
        // scroll_down.style.transform = "translateY(10px)";
        scroll_down.style.opacity = "1";
    }
}
 

// splash screen counter 
var count_number = 0; 
let preloader_counter_function = setInterval(function(){
    count_number++;
    preloader_counter.innerHTML = count_number; 
    
    if (count_number == 100){
        clearInterval(preloader_counter_function);
    }
},12) 


// window change color and background
window.onclick = () => {
   let arr = ["css/blue.css", "", "css/red.css", "", "css/green.css", "", "css/yellow.css", "", "css/gray.css", "", "css/pink.css", "", "css/cyan.css", "", "css/green2.css", "", "css/red.css", "css/red2.css", "css/blue2.css" ]
    window.style.zIndex = -9999;
   let styleSheet = arr[Math.floor(Math.random() * arr.length)];
   style.setAttribute("href", styleSheet);
}



// mousemove code  
window.onmousemove  = () => {
            var a = document.createElement("p");
            a.setAttribute("id", "mousemove");
            document.body.appendChild(a);
            a.style.left = event.clientX + 'px';
            a.style.top = event.clientY + 'px';
            var col = ["yellow","green","blue","red"];
            var mcol = col[Math.floor(Math.random()*col.length)];
            a.style.transition = "all 1s linear";
            a.style.left = a.offsetLeft - 20 + "px";
           a.style.top = a.offsetTop - 20 + "px";
           a.style.height = "50px";
           a.style.width = "50px";
           a.style.borderWidth = "2px"; 
           a.style.opacity = 0;
           a.style.borderColor = mcol;
          }


// service worker 

//////////// its service worker part ////////////

if('serviceWorker' in navigator) {
    navigator.serviceWorker.register('../sw.js')
    .then(res => {
      console.info('Service Worker is Regitser', res);
    })
    .catch(err => {
      console.info('Service Worker is not Register', err);
    })
  } else 
    console.log('Service Worker is not suppoted in your browser');
  
  
  


 
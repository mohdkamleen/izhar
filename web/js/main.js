let preloader = document.querySelector("div.preloader"); 
let preloader_counter = document.querySelector("div.preloader span b"); 
let nav_hamberger_background = document.querySelector("section .body_content_header .nav_hamburger_background"); 

window.onload = () => {
    preloader.classList.add("active"); 
}  

window.onscroll = () => {
    let windowPageYOffset = window.pageYOffset;
    if(windowPageYOffset > 400){
        nav_hamberger_background.classList.add("show");
    } else {
        nav_hamberger_background.classList.remove("show");
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
},25) 






 
let preloader = document.querySelector("div.preloader"); 
let preloader_counter = document.querySelector("div.preloader span b"); 
let nav_hamberger_background = document.querySelector(".nav_hamburger_background"); 
let scroll_down = document.querySelector(" .scroll_down");  

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






 
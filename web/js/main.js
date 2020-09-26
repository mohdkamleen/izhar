let preloader = document.querySelector("div.preloader"); 
let preloader_counter = document.querySelector("div.preloader span b"); 
let nav_hamberger_background = document.querySelector(".nav_hamburger_background"); 
let scroll_down = document.querySelector(".scroll_down"); 
// let main_div = document.querySelector("#main_div"); 

window.onload = () => {
    preloader.classList.add("active"); 
}  

// window.onresize = () => {
//     if(window.innerWidth > 1000){
//         main_div.setAttribute("id", "main_page");
//     } 
// }

window.onscroll = () => {
    let windowPageYOffset = window.pageYOffset;
    if(windowPageYOffset > 400){
        nav_hamberger_background.classList.add("show");
    } else {
        nav_hamberger_background.classList.remove("show");
    }

    if(windowPageYOffset > 10){
        scroll_down.style.top = "90%";
        scroll_down.style.opacity = "0"; 
    } else {
        scroll_down.style.top = "80%";
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






 
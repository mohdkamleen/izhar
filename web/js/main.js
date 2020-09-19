let preloader = document.querySelector("div.preloader"); 
let preloader_counter = document.querySelector("div.preloader span b"); 

window.onload = () => {
    preloader.classList.add("active"); 
}  
 
setInterval(function(){
    var count_number = 0; 
    count_number++;
    preloader_counter.innerHTML = count_number; 
},1000) 



// let preloader_counter_function;  
 
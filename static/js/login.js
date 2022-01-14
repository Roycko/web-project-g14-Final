
function open_login(){
    document.querySelector(".popup").style.display="flex";
    $('html, body').animate({ scrollTop: 0 }, 'fast');
}
function close_login(){
    document.querySelector(".popup").style.display="none";
}
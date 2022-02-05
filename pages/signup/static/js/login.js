
function open_login(){
    document.querySelector(".popup").style.display="flex";
    $('html, body').animate({ scrollTop: 0 }, 'fast');
}
function close_login(){
    document.querySelector(".popup").style.display="none";
}
function close_login(){
    document.querySelector(".popup").style.display="none";
}
function change_value(product_id){
    document.getElementsByName("submit"+product_id).value=product_id;
}
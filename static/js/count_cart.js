

const minusButton = document.getElementById('minus');
const plusButton = document.getElementById('plus');
const inputField = document.getElementById('input');

// window.onload = tPrice;
minusButton.addEventListener('click', event => {
    event.preventDefault();
    const currentValue = Number(inputField.value) || 0;
    if (currentValue >= 1) {
        inputField.value = currentValue - 1;
    }
});

plusButton.addEventListener('click', event => {
    event.preventDefault();
    const currentValue = Number(inputField.value) || 0;
    inputField.value = currentValue + 1;
});
function action(product_id,action,price){
    var inputEl = document.getElementById('input_'+product_id);
    if (action==='plus'){
     inputEl.value= parseInt(inputEl.value)+1;
    }
    else{
        if (parseInt(inputEl.value)>0){
            inputEl.value= parseInt(inputEl.value)-1;
        }
    }
    tPrice(parseInt(price),parseInt(inputEl.value));
    console.log(product_id);
}
function tPrice(price,quantity){
    finalPrice = Number(document.getElementById("totalPrice").value);
    finalPrice += price*quantity;
}
// function tPrice() {
//     pr1 = document.getElementById("unitPrice1").innerHTML.substring(0,document.getElementById("unitPrice1").innerHTML.length-2);
//     pr2 = document.getElementById("unitPrice2").innerHTML.substring(0,document.getElementById("unitPrice2").innerHTML.length-2);
//     pr3 = document.getElementById("unitPrice3").innerHTML.substring(0,document.getElementById("unitPrice3").innerHTML.length-2);
//
//     fp1 = pr1*Number(document.getElementById("n1").value) + pr2*Number(document.getElementById("n2").value) + pr3*Number(document.getElementById("n3").value)
//     document.getElementById("totalPrice").innerHTML = fp1 + "$"
// }
// function plus(product){
//     product.parentNode.value++;
//     console.log("Hi");
// // }
//
// function p1(){
//         document.getElementById("n1").value++;
//     tPrice();
// }
//
// function p2(){
//     document.getElementById("n2").value ++;
//     tPrice();
// }
// function p3(){
//     document.getElementById("n3").value ++;
//     tPrice();
// }
//
// function p4(){
//     document.getElementById("n4").value++;
//     tPrice();
// }
//
// function p5(){
//     document.getElementById("n5").value++;
//     tPrice();
// }
//
// function p6(){
//     document.getElementById("n6").value++;
//     tPrice();
// }
// function p7(){
//     document.getElementById("n7").value++;
//     tPrice();
// }
// function p8(){
//     document.getElementById("n8").value++;
//     tPrice();
// }
// function p9(){
//     document.getElementById("n9").value++;
//     tPrice();
// }
//
//
//
// function m1(){
//     if (document.getElementById("n1").value > 0)
//         document.getElementById("n1").value --;
//     tPrice();
// }
// function m2(){
//     if (document.getElementById("n2").value > 0)
//         document.getElementById("n2").value --;
//     tPrice();
// }
// function m3(){
//     if (document.getElementById("n3").value > 0)
//         document.getElementById("n3").value --;
//     tPrice();
// }
// function m4(){
//     if (document.getElementById("n4").value > 0)
//         document.getElementById("n4").value --;
// }
// function m5(){
//     if (document.getElementById("n5").value > 0)
//         document.getElementById("n5").value --;
// }
// function m6(){
//     if (document.getElementById("n6").value > 0)
//         document.getElementById("n6").value --;
// }
// function m7(){
//     if (document.getElementById("n7").value > 0)
//         document.getElementById("n7").value --;
// }
// function m8(){
//     if (document.getElementById("n8").value > 0)
//         document.getElementById("n8").value --;
// }
// function m9(){
//     if (document.getElementById("n9").value > 0)
//         document.getElementById("n9").value --;
// }
//
//

//
//
// function remove(card){
//     card.parentNode.parentNode.parentNode.remove();
// }




function p1(){
        document.getElementById("n1").value++;
    tPrice();
}

function p2(){
    document.getElementById("n2").value ++;
    tPrice();
}
function p3(){
    document.getElementById("n3").value ++;
    tPrice();
}

function p4(){
    document.getElementById("n4").value++;
    tPrice();
}

function p5(){
    document.getElementById("n5").value++;
    tPrice();
}

function p6(){
    document.getElementById("n6").value++;
    tPrice();
}
function p7(){
    document.getElementById("n7").value++;
    tPrice();
}
function p8(){
    document.getElementById("n8").value++;
    tPrice();
}
function p9(){
    document.getElementById("n9").value++;
    tPrice();
}

function m1(){
    if (document.getElementById("n1").value > 0)
        document.getElementById("n1").value --;
    console.log("hi2");
    tPrice();
}
function m2(){
    if (document.getElementById("n2").value > 0)
        document.getElementById("n2").value --;
    tPrice();
}
function m3(){
    if (document.getElementById("n3").value > 0)
        document.getElementById("n3").value --;
    tPrice();
}
function m4(){
    if (document.getElementById("n4").value > 0)
        document.getElementById("n4").value --;
}
function m5(){
    if (document.getElementById("n5").value > 0)
        document.getElementById("n5").value --;
}
function m6(){
    if (document.getElementById("n6").value > 0)
        document.getElementById("n6").value --;
}
function m7(){
    if (document.getElementById("n7").value > 0)
        document.getElementById("n7").value --;
}
function m8(){
    if (document.getElementById("n8").value > 0)
        document.getElementById("n8").value --;
}
function m9(){
    if (document.getElementById("n9").value > 0)
        document.getElementById("n9").value --;
}


function tPrice() {
    pr1 = document.getElementById("unitPrice1").innerHTML.substring(0,document.getElementById("unitPrice1").innerHTML.length-2);
    pr2 = document.getElementById("unitPrice2").innerHTML.substring(0,document.getElementById("unitPrice2").innerHTML.length-2);
    pr3 = document.getElementById("unitPrice3").innerHTML.substring(0,document.getElementById("unitPrice3").innerHTML.length-2);

    fp1 = pr1*Number(document.getElementById("n1").value) + pr2*Number(document.getElementById("n2").value) + pr3*Number(document.getElementById("n3").value)
    document.getElementById("totalPrice").innerHTML = fp1 + "$"
}
window.onload = tPrice;


function remove(card){
    card.parentNode.parentNode.parentNode.remove();
}

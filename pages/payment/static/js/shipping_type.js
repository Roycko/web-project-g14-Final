 function onShippingMethodChange(){
    debugger;
    var value = document.getElementById("shippingMethod").value;
    var visibilityValue = value === "delivery" ? 'visible' : 'hidden';
    document.getElementById("addressContainer").style.visibility = visibilityValue;
}

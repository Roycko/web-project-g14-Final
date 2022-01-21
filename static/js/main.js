(function ($) {
    "use strict";
    //Loader
    jQuery(window).on("load", function () {
        jQuery(".loader").fadeOut(1000);
    });
}(jQuery));

function addToCart(button){
    button.innerHTML = "Added to Cart";
    button.style.cursor = "initial";
    button.style.backgroundColor = "Grey";
    button.disabled = true;
}


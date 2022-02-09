function ValiditionExistingEvent() {
   console.log('start Val ExistingEvent');
        var inpObj = document.getElementById("event_name");
        var inpObj2 = document.getElementById("event_date");
        var inpObj3 = document.getElementById("Amount");
        var inpObj4 = document.getElementById("fname");
        var inpObj5 = document.getElementById("Lname");
        var inpObj6 = document.getElementById("email");
        var inpObj7 = document.getElementById("Phone");


        if(!inpObj3 || !inpObj4 || !inpObj5 || !inpObj6 || !inpObj7){
            document.getElementById("mandatoryX").innerHTML = 'fill ALL the field';
            return false;
        }
}

function ValiditionPrivteEvent() {
    console.log('start Val PrivteEvent');
        var inpObjP = document.getElementById("p_event_name");
        var inpObjP2 = document.getElementById("p_event_date");
        var inpObjP3 = document.getElementById("PAmount");
        var inpObjP4 = document.getElementById("Pfname");
        var inpObjP5 = document.getElementById("PLname");
        var inpObjP6 = document.getElementById("Pemail");
        var inpObjP7 = document.getElementById("PPhone");


        if(!inpObjP || !inpObjP2 || !inpObjP3 || !inpObjP4 || !inpObjP5 || !inpObjP6 || !inpObjP7){
            document.getElementById("mandatoryP").innerHTML = 'fill ALL the field';
            return false;
        }
}
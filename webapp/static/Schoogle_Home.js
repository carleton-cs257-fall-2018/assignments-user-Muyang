/*
    Schoogle_Home.js
    Muyang Shi, 27 Oct 2018
 */


window.onload = initialize();

function onButtonPress() {
    alert('Lead you to the result page!');
}

function initialize() {
    var button = document.getElementById('searchButton');
    button.onclick = onButtonPress;
}




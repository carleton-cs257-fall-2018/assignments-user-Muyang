/*
    Schoogle_Home.js
    Muyang Shi, 27 Oct 2018
 */
function onButtonPress() {
    alert('Lead you to result page!');
}

function initialize() {
    var button = document.getElementById('searchButton');
    button.onclick = onButtonPress;
}

window.onload = initialize;


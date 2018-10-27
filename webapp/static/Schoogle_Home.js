/*
	Schoogle_Home.js
	Muyang Shi, 27 Oct 2018
 */

function onSearchButtonPress() {
	alert('something else');
	var url = getBaseURL() + '/schools';

	// Send the request to the Schoogl API /schools endpoint
	fetch(url, {method: 'get'})

	.then((response) => response.json())
}

function initialize() {
	var button = document.getElementById('searchButton');
	if (button){
		button.onclick = onSearchButtonPress;
	}
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + '5001';
	return baseURL;
}

window.onload = initialize;
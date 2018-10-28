/*
	Schoogle_Home.js
	Muyang Shi, 27 Oct 2018
 */


function getSchool(schoolID) {
	// Very similar pattern to onAuthorsButtonClicked, so I'm not
	// repeating those comments here. Read through this code
	// and see if it makes sense to you.
	var url = getBaseURL() + '/schools?school_id =' + schoolID;

	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		var tableBody = '<tr><th>' + 'Results' + '</th></tr>';
		for (var k = 0; k < schoolsList.length; k++) {
			tableBody += '<tr>';
			tableBody += '<td>' + schoolsList[k]['school_name'] + '</td>';
			tableBody += '<td>' + schoolsList[k]['city'] + '</td>';
			tableBody += '</tr>';
		}
		var resultsTableElement = document.getElementById('results_table');
		if (resultsTableElement) {
			resultsTableElement.innerHTML = tableBody;
		}
	})

	.catch(function(error) {
		console.log(error);
	});
}








function onSearchButtonPress() {
	alert('something else');
	var url = getBaseURL() + '/schools';

	// Send the request to the Schoogl API /schools endpoint
	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		// Build the table body.
		var tableBody = '';
		for (var k = 0; k < schoolsList.length; k++) {
			tableBody += '<tr>';
			tableBody += '<td>' + schoolsList[k]['school_id'] + '</td>';
			tableBody += '<td>' + schoolsList[k]['school_name'] + '</td>';
			tableBody += '<td>' + schoolsList[k]['city'] + '</td>'; 
			tableBody += '<td>' + schoolsList[k]['enrollment'] + '</td>';
			tableBody += '</tr>';
		}

		// Put the table body we just built inside the table that's already on the page.
		var schools = document.getElementById('results_table');
		if (schools) {
			schools.innerHTML = tableBody;
		}
	})
}

function initialize() {
	var button = document.getElementById('searchButton');
	if (button){
		button.onclick = onSearchButtonPress;
	}
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}

window.onload = initialize;
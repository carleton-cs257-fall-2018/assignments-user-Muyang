/*
	Schoogle_Home.js
	Muyang Shi, 27 Oct 2018
 */

function onHomeButtonPress() {
	location.reload();
}

function onSearchButtonPress() {
	var searchBarText = document.getElementById('searchBar')
	
	var url = getBaseURL() + '/schools' + '?school_name=' + searchBarText.value;

	// Send the request to the Schoogl API /schools endpoint
	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		// Build the table body.
		var tableBody = '<tr><th align="left">' + 'Results for "' + searchBarText.value + '"' +'</th></tr>';
		//column header
		tableBody += '<tr><td>Check To Compare</td><td>School ID</td> <td>School Name</td> <td>City</td> <td>Enrollment</td>'
		for (var k = 0; k < schoolsList.length; k++) {
			tableBody += '<tr>';
			tableBody += '<td>' + '<input type="checkbox" id=checkbox' + k + '>' 
						+ '</td>';
			tableBody += '<td>' + schoolsList[k]['school_id'] + '</td>';
			tableBody += '<td>' + schoolsList[k]['school_name'] + '</td>';
			tableBody += '<td>' + schoolsList[k]['city'] + '</td>'; 
			tableBody += '<td>' + schoolsList[k]['enrollment']  + '</td>';
			tableBody += '<td><a onclick="seeMore(' + schoolsList[k]['school_id'] + ',\'' + searchBarText.value +'\')">' + '<button id="seeMoreButton"> See More </button>' + '</a>' + '</td>';
			tableBody += '</tr>';
		}


		// Put the table body we just built inside the table that's already on the page.
		var schools = document.getElementById('results_table');
		if (schools) {
			schools.innerHTML = tableBody;
		}
	})

	// Log the error if anything went wrong during the fetch.
	.catch(function(error) {
		console.log(error);
	});

	document.getElementById('initialDropdown').style.display = 'none';
}


function onReturnButtonPress(returnSearch) {
	//redo the search
	document.getElementById("searchBar").innerHTML.value = returnSearch
	//show the search bar and the search button
	document.getElementById("searchBar").style.display = "initial";
	document.getElementById("searchButton").style.display = "initial";
	document.getElementById("compareButton").style.display = "initial";
	//hide the return button
	document.getElementById('returnResultsButton').style.display = "none";
	onSearchButtonPress();
}

function onCompareButtonPress(){
	var table = document.getElementById("results_table");
	var school_id_list = [];
	for (var i=2, row; row = table.rows[i]; i++){
		var k = i-2;
		if(document.getElementById("checkbox" + k).checked){
			school_id_list.push(row.cells[1].innerHTML);
		}
	}
	var id_string = '';
	for(var i =0; i< school_id_list.length; i++){
		if(i > 0){
			id_string += ',';
		}
		id_string += school_id_list[i];
	}

	var url = getBaseURL() + '/schools' + '?school_id=' + id_string;

	// Send the request to the Schoogl API /schools endpoint
	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		var tableBody = _addTableHeader(schoolsList);
		tableBody = _addTableRow(tableBody, schoolsList, 'school_name');
		tableBody = _addTableRow(tableBody, schoolsList, 'city');
		tableBody = _addTableRow(tableBody, schoolsList, 'state_name');
		tableBody = _addTableRow(tableBody, schoolsList, 'highest_degree');
		tableBody = _addTableRow(tableBody, schoolsList, 'locale');
		tableBody = _addTableRow(tableBody, schoolsList, 'ownership');
		tableBody = _addTableRow(tableBody, schoolsList, 'SAT_average');
		tableBody = _addTableRow(tableBody, schoolsList, 'ACT_cumulative_MID');
		tableBody = _addTableRow(tableBody, schoolsList, 'admission_rate');
		tableBody = _addTableRow(tableBody, schoolsList, 'enrollment');
		var schools = document.getElementById('results_table');
		if (schools) {
			schools.innerHTML = tableBody;
		}
	})

	.catch(function(error) {
		console.log(error);
	});



	
	document.getElementById('returnResultsButton').style.display = "none";
	document.getElementById('returnResultsButton').onclick= function() {onReturnButtonPress(returnSearch);};
	document.getElementById('searchBar').style.display = "none";
	document.getElementById('searchButton').style.display = "none";
	document.getElementById('compareButton').style.display = "none";	

}
function onAdvancedButtonPress(){
	var advanced_search_table = document.getElementById('advanced_search_table');
	var tableBody = '<tr><th align="left">' + 'Advanced Options' + '</th><tr>';
	tableBody += '<tr>' + '<td>Admission Rate</td>' + '<input type="text" id="admission_rate_small" placeholder="0.0" value="0.0">'
	tableBody += '</tr';
}


function seeMore(schoolID, returnSearch) {
	// Very similar pattern to onAuthorsButtonClicked, so I'm not
	// repeating those comments here. Read through this code
	// and see if it makes sense to you.
	var url = getBaseURL() + '/schools?school_id=' + schoolID;

	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		var school = schoolsList[0];
		var tableBody = '<tr><th>' + 'More Info about ' + school['school_name'] +  '</th></tr>';
		tableBody = _addTableRow(tableBody, schoolsList, 'school_name');
		tableBody = _addTableRow(tableBody, schoolsList, 'city');
		tableBody = _addTableRow(tableBody, schoolsList, 'state_name');
		tableBody = _addTableRow(tableBody, schoolsList, 'highest_degree');
		tableBody = _addTableRow(tableBody, schoolsList, 'locale');
		tableBody = _addTableRow(tableBody, schoolsList, 'ownership');
		tableBody = _addTableRow(tableBody, schoolsList, 'SAT_average');
		tableBody = _addTableRow(tableBody, schoolsList, 'ACT_cumulative_MID');
		tableBody = _addTableRow(tableBody, schoolsList, 'admission_rate');
		tableBody = _addTableRow(tableBody, schoolsList, 'enrollment');
		
		var resultsTableElement = document.getElementById('results_table');
		if (resultsTableElement) {
			resultsTableElement.innerHTML = tableBody;
		}
	})

	.catch(function(error) {
		console.log(error);
	});
	document.getElementById('returnResultsButton').style.display = "block";
	document.getElementById('returnResultsButton').onclick= function() {onReturnButtonPress(returnSearch);};
	document.getElementById('searchBar').style.display = "none";
	document.getElementById('searchButton').style.display = "none";
	document.getElementById('compareButton').style.display = "none";

}


function initialize() {
	var searchButton = document.getElementById('searchButton');
	var compareButton = document.getElementById('compareButton');
	var homeButton = document.getElementById('homeButton')
	var input = document.getElementById('searchBar');
	var advancedButton = document.getElementById('advanced');

	document.getElementById('returnResultsButton').style.display = "none";
	input.addEventListener("keyup", function() {_enterPressed(event);});

	_setOnClick(searchButton, onSearchButtonPress);
	_setOnClick(compareButton, onCompareButtonPress);
	_setOnClick(homeButton, onHomeButtonPress);
	_setOnClick(advancedButton, onAdvancedButtonPress);
	
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}


function _enterPressed(event) {
	event.preventDefault();
		if (event.keyCode === 13) {
    		searchButton.click();
		}
}

function _setOnClick(button, action){
	if(button) {
		button.onclick = action
	}
}


function _addTableHeader(schoolsList) {
	var tableBody = '<tr><th> Comparison Between: </th>';
	for(var i= 0; i <schoolsList.length; i++){
		tableBody += '<th>' + schoolsList[i]['school_name'] + '</th>';
	}
	tableBody += '</tr>';
	return tableBody;


}

function _addTableRow(tableBody, schoolsList, metric){
	display_metric = _convertMetricName(metric);
	tableBody += '<tr>';
	tableBody += '<td>'+ display_metric + '</td>';
		for(var i = 0; i < schoolsList.length; i++){
			tableBody +='<td>' + schoolsList[i][metric] + '</td>';
		}
		tableBody += '</tr>';
	return tableBody;
}

function _convertMetricName(metric){
	var display_metric = '';
	var new_word = true;
	for(var i = 0; i <metric.length; i++){
		if (new_word){
			display_metric += metric.charAt(i).toUpperCase();
			new_word = false
		}else if(metric.charAt(i) =='_'){
			display_metric += ' '
			new_word = true
		}else{
			display_metric += metric.charAt(i);
		}
	}	
	return display_metric;	
}

window.onload = initialize;
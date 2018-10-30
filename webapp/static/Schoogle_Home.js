/*
	Schoogle_Home.js
	Muyang Shi, 27 Oct 2018
 */

function onHomeButtonPress() {
	location.reload();
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


function seeMore(schoolID, returnSearch) {
	// Very similar pattern to onAuthorsButtonClicked, so I'm not
	// repeating those comments here. Read through this code
	// and see if it makes sense to you.
	var url = getBaseURL() + '/schools?school_id=' + schoolID;

	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		var school = schoolsList[0]
		var tableBody = '<tr><th>' + 'Advanced Info about ' + school['school_name'] +  '</th></tr>';
		tableBody += '<tr><td>Name:</td><td>' + school['school_name'] + '</td></tr>';
		tableBody += '<tr><td>City:</td><td>' + school['city'] + '</td></tr>';
		tableBody += '<tr><td>State:</td><td>' + school['state_name'] + '</td></tr>';
		tableBody += '<tr><td>Highest Degree:</td><td>' + school['highest_degree'] + '</td></tr>';
		tableBody += '<tr><td>Locale:</td><td>' + school['locale'] + '</td></tr>';
		tableBody += '<tr><td>Ownership:</td><td>' + school['ownership'] + '</td></tr>';
		tableBody += '<tr><td>SAT Average:</td><td>' + school['SAT_average'] + '</td></tr>';

		tableBody += '<tr><td>ACT Average:</td><td>' + school['ACT_cumulative_MID'] + '</td></tr>';
		tableBody += '<tr><td>Admission Rate:</td><td>' + school['admission_rate'] + '</td></tr>';
		tableBody += '<tr><td>Enrollment:</td><td>' + school['enrollment'] + '</td></tr>';
		

		
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
	for (var j = 0; j < school_id_list.length; j++){
		var url = getBaseURL() + '/schools?school_id=' + school_id_list[j];

		fetch(url, {method: 'get'})

		.then((response) => response.json())

		.then(function(schoolsList) {
			var school = schoolsList[0]
			var tableBody = '<tr><th>' + 'Advanced Info about ' + school['school_name'] +  '</th></tr>';
			tableBody += '<tr><td>Name:</td><td>' + school['school_name'] + '</td></tr>';
			tableBody += '<tr><td>City:</td><td>' + school['city'] + '</td></tr>';
			tableBody += '<tr><td>State:</td><td>' + school['state_name'] + '</td></tr>';
			tableBody += '<tr><td>Highest Degree:</td><td>' + school['highest_degree'] + '</td></tr>';
			tableBody += '<tr><td>Locale:</td><td>' + school['locale'] + '</td></tr>';
			tableBody += '<tr><td>Ownership:</td><td>' + school['ownership'] + '</td></tr>';
			tableBody += '<tr><td>SAT Average:</td><td>' + school['SAT_average'] + '</td></tr>';

			tableBody += '<tr><td>ACT Average:</td><td>' + school['ACT_cumulative_MID'] + '</td></tr>';
			tableBody += '<tr><td>Admission Rate:</td><td>' + school['admission_rate'] + '</td></tr>';
			tableBody += '<tr><td>Enrollment:</td><td>' + school['enrollment'] + '</td></tr>';
			

			
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
}








function initialize() {
	var searchButton = document.getElementById('searchButton');
	var input = document.getElementById('searchBar');
	document.getElementById('returnResultsButton').style.display = "none";

	//go back to home page
	document.getElementById('homeButton').onclick = onHomeButtonPress;

	//search something and hit enter, or the user clicke the searchButton
	input.addEventListener("keyup", function(event) {
    	event.preventDefault();
    		if (event.keyCode === 13) {
        		searchButton.click();
    		}
	});
	if (searchButton){
		searchButton.onclick = onSearchButtonPress;
	}

	var compareButton = document.getElementById('compareButton');
	if (compareButton){
		compareButton.onclick = onCompareButtonPress;
	}
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}

window.onload = initialize;
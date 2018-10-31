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

	//as long as the advanced option is opened
	if(document.getElementById('admission_rate_small')){
		var admission_rate_small = document.getElementById('admission_rate_small').value;
		var admission_rate_large = document.getElementById('admission_rate_large').value;

		url += '&admission_rate=' + admission_rate_small + '..' + admission_rate_large;

		var enrollment_small = document.getElementById('enrollment_small').value;
		var enrollment_large = document.getElementById('enrollment_large').value;

		url += '&enrollment=' + enrollment_small + '..' + enrollment_large;

		var highest_degree = document.getElementById('highest_degree').value;
		url += '&highest_degree=' + highest_degree;

		var state_name = document.getElementById('state_name').value;
		url += '&state_name=' + state_name;

		var average_faculty_earnings = document.getElementById('average_faculty_earnings').value;
		url += '&average_faculty_earnings=' + average_faculty_earnings + '..';

		var major = document.getElementById('program').value;
		if (major != 'Any'){
			url += '&' + major + '=True';
		}
	}




	// Send the request to the Schoogl API /schools endpoint
	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(schoolsList) {
		// Build the table body.
		var tableBody = '<tr><th align="center">' + 'Results' +'</th></tr>';
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

	document.getElementById('compareButton').style.display = "initial";
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
		if(schoolsList.length == 0){
			alert("Check boxes to select which schools to compare")

		}
		else{
			var tableBody = _addTableHeader(schoolsList);
			tableBody = _addTableRow(tableBody, schoolsList, 'city');
			tableBody = _addTableRow(tableBody, schoolsList, 'state_name');
			tableBody = _addTableRow(tableBody, schoolsList, 'highest_degree');
			tableBody = _addTableRow(tableBody, schoolsList, 'locale');
			tableBody = _addTableRow(tableBody, schoolsList, 'ownership');
			tableBody = _addTableRow(tableBody, schoolsList, 'SAT_average');
			tableBody = _addTableRow(tableBody, schoolsList, 'ACT_cumulative_MID');
			tableBody = _addTableRow(tableBody, schoolsList, 'admission_rate');
			tableBody = _addTableRow(tableBody, schoolsList, 'enrollment');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_student_of_Pell_Grant');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_student_of_Federal_Loan');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_white');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_black');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_Hispanic');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_Asian');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_American_Indian');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_Native_Hawaiian');
			tableBody = _addTableRow(tableBody, schoolsList, 'percent_nonresident_aliens');
			tableBody = _addTableRow(tableBody, schoolsList, 'average_faculty_earning');
			var schools = document.getElementById('results_table');
			if (schools) {
				schools.innerHTML = tableBody;
			}
			document.getElementById('returnResultsButton').style.display = "none";
			document.getElementById('returnResultsButton').onclick= function() {onReturnButtonPress(returnSearch);};
			document.getElementById('searchBar').style.display = "none";
			document.getElementById('searchButton').style.display = "none";
			document.getElementById('compareButton').style.display = "none";
			document.getElementById('advanced').style.display = 'none';
			document.getElementById('advanced_search_table').style.display = 'none';
			
		}
	})

	.catch(function(error) {
		console.log(error);
	});

		

}
function onAdvancedButtonPress(){
	var tableBody = '<tr><th align="left">' + 'Advanced Options' + '</th><tr>';
	tableBody += '<tr>' + '<td>Admission Rate</td>' 
						+ '<td><input type="text" id="admission_rate_small" placeholder="0.0" value="0.0">'
						+ ' to '
						+ '<input type="text" id="admission_rate_large" placeholder="1.0" value="1.0">'
						+ '</td>'
				+'</tr>';
	tableBody += '<tr>' + '<td>Enrollment</td>' 
						+ '<td><input type="text" id="enrollment_small" placeholder="0" value="0">'
						+ ' to '
						+ '<input type="text" id="enrollment_large" placeholder="MAX" value="">'
						+ '</td>'
				+'</tr>';			
	tableBody += '<tr>' + '<td>Program</td>' 
						+ '<td><select id="program" value="">'
						+ '<option value="Any"> Any </option>'			
						+ '<option value="Agriculture">Agriculture, Agriculture Operations, and Related Sciences</option>'

						+ '<option value="Architecture">Architecture and Related Services</option>'
						
						+ '<option value="Area_Ethnic_Cultural_Gender_Group_Studies">Area, Ethnic, Cultural, Gender, and Group Studies</option>'
						
						+ '<option value="Biological_and_Biomedical_Sciences">Biological and Biomedical Sciences</option>'
						
						+ '<option value="Business_Management_Marketing">Business, Management, Marketing, and Related Support Services</option>'
						
						+ '<option value="Communication_Journalism">Communication, Journalism, and Related Programs</option>'
						
						+ '<option value="Communication_Technologies">Communications Technologies/Technicians and Support Services</option>'
						
						+ '<option value="Computer_Information_Sciences">Computer and Information Sciences and Support Services</option>'
						
						+ '<option value="Construction_Trade">Construction Trades</option>'
						
						+ '<option value="Education">Education</option>'
						
						+ '<option value="Engineering">Engineering</option>'
						
						+ '<option value="Engineering_Technologies">Engineering Technologies and Engineering-Related Fields</option>'
						
						+ '<option value="English_Language_And_Literature">English Language and Literature/Letters</option>'
						
						+ '<option value="family_consumer_science">Family and Consumer Sciences</option>'

						+ '<option value="Human_Sciences">Human Sciences</option>'
						
						+ '<option value="Foreign_Languages_Literatures_Linguistics">Foreign Languages, Literatures, and Linguistics</option>'
						
						+ '<option value="Health_Professions">Health Professions and Related Programs</option>'
						
						+ '<option value="History">History</option>'
						
						+ '<option value="Homeland_Security_Law_Enforcement_Firefighting">Homeland Security, Law Enforcement, Firefighting and Related Protective Services</option>'
						
						+ '<option value="Legal_Professions_Studies">Legal Professions and Studies</option>'
						
						+ '<option value="General_Studies_And_Humanities">Liberal Arts and Sciences, General Studies and Humanities</option>'
						
						+ '<option value="Library_Science">Library Science</option>'
						
						+ '<option value="Mathematics_and_Statistics">Mathematics and Statistics</option>'
						
						+ '<option value="Mechanic_and_Repair_Technology">Mechanic and Repair Technologies/Technicians</option>'
						
						+ '<option value="Military_Technologies_and_Applied_Sciences">Military Technologies and Applied Sciences</option>'
						
						+ '<option value="Interdiciplinary_Studies">Multi/Interdisciplinary Studies</option>'
						
						+ '<option value="Natural_Resource">Natural Resources and Conservation</option>'
						
						+ '<option value="Parks_Recreation_Leisure_Fitness_Studies">Parks, Recreation, Leisure, and Fitness Studies</option>'
						
						+ '<option value="Personal_Culinary_Services">Personal and Culinary Services</option>'
						
						+ '<option value="Philosophy_and_Religious_Studies">Philosophy and Religious Studies</option>'
						
						+ '<option value="Physical_Sciences">Physical Sciences</option>'
						
						+ '<option value="Precision_Production">Precision Production</option>'
						
						+ '<option value="Psychology">Psychology</option>'
						
						+ '<option value="Public_Administration_and_Social_Service">Public Administration and Social Service Professions</option>'
						
						+ '<option value="Science_Technologies">Science Technologies/Technicians</option>'
						
						+ '<option value="Social_Sciences">Social Sciences</option>'
						
						+ '<option value="Theology_and_Religious_Vocations">Theology and Religious Vocations</option>'
						
						+ '<option value="Transportation_and_Materials_Moving">Transportation and Materials Moving</option>'
						
						+ '<option value="Visual_and_Performing_Arts">Visual and Performing Arts</option>'
				+ '</td>'
				+'</tr>';
	tableBody += '<tr>' + '<td>Highest Degree</td>' 
						+ '<td><select id="highest_degree" value="">'
						+ '<option value="">Any</option>'
						+ '<option value="bachelor">Bachelor</option>'
						+ '<option value="Non-degree-granting">Non-degree-granting</option>'
						+ '<option value="Certificate">Certificate</option>'
						+ '<option value="Associate">Associate</option>'
						+ '<option value="Graduate">Graduate</option>'
						+ '</td>'
				+'</tr>';
	tableBody += '<tr>' + '<td>State Name</td>' 
						+ '<td><input type="text" id="state_name" placeholder="name of the state" value="">'
						+ '</td>'
				+'</tr>';
	tableBody += '<tr>' + '<td>Average Faculty Earnings</td>' 
						+ '<td><input type="text" id="average_faculty_earnings" placeholder="minimum amount" value="">'
						+ '</td>'
				+'</tr>';

	var table = document.getElementById('advanced_search_table');
	if (table) {
		table.innerHTML = tableBody;
	}
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
		var tableBody = '<tr><th>' + school['school_name'] +  '</th></tr>';
		tableBody = _addTableRow(tableBody, schoolsList, 'city');
		tableBody = _addTableRow(tableBody, schoolsList, 'state_name');
		tableBody = _addTableRow(tableBody, schoolsList, 'highest_degree');
		tableBody = _addTableRow(tableBody, schoolsList, 'locale');
		tableBody = _addTableRow(tableBody, schoolsList, 'ownership');
		tableBody = _addTableRow(tableBody, schoolsList, 'SAT_average');
		tableBody = _addTableRow(tableBody, schoolsList, 'ACT_cumulative_MID');
		tableBody = _addTableRow(tableBody, schoolsList, 'admission_rate');
		tableBody = _addTableRow(tableBody, schoolsList, 'enrollment');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_student_of_Pell_Grant');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_student_of_Federal_Loan');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_white');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_black');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_Hispanic');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_Asian');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_American_Indian');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_Native_Hawaiian');
		tableBody = _addTableRow(tableBody, schoolsList, 'percent_nonresident_aliens');
		tableBody = _addTableRow(tableBody, schoolsList, 'average_faculty_earning');
		
		var resultsTableElement = document.getElementById('results_table');
		if (resultsTableElement) {
			resultsTableElement.innerHTML = tableBody;
		}
	})

	.catch(function(error) {
		console.log(error);
	});
	document.getElementById('returnResultsButton').style.display = "initial";
	document.getElementById('returnResultsButton').onclick= function() {onReturnButtonPress(returnSearch);};
	document.getElementById('searchBar').style.display = "none";
	document.getElementById('searchButton').style.display = "none";
	document.getElementById('compareButton').style.display = "none";
	document.getElementById('advanced').style.display = 'none';
	document.getElementById('advanced_search_table').style.display = 'none';

}


function initialize() {
	var searchButton = document.getElementById('searchButton');
	var compareButton = document.getElementById('compareButton');
	var homeButton = document.getElementById('homeButton')
	var input = document.getElementById('searchBar');
	var advancedButton = document.getElementById('advanced');

	document.getElementById('returnResultsButton').style.display = "none";
	document.getElementById('compareButton').style.display = "none";
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
			tableBody +='<td align="center">'
			if(String(schoolsList[i][metric]) == 'undefined' || String(schoolsList[i][metric]) == 'null') {
				tableBody += '--' + '</td>'
			}
			else{
				tableBody += schoolsList[i][metric] + '</td>';
			}
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
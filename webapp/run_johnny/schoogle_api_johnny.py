#!/usr/bin/env python3
'''
	schoogle_api.py
	Johnny Reichman and Muyang Shi, 21 Oct 2018

'''
import sys
import flask
import json
import config_johnny
import psycopg2

app = flask.Flask(__name__)
basic_list = ['school_id' ,'school_name', 'city','state_name','school_url','highest_degree','locale','ownership']
stats_list = [
	'school_id',
	'year',
	'admission_rate',

	'SAT_average',
	'SAT_cr_MID',
	'SAT_cr_25_percentile',
	'SAT_cr_75_percentile',
	'SAT_math_MID',
	'SAT_math_25_percentile',
	'SAT_math_75_percentile',
	'SAT_wr_MID',
	'SAT_wr_25_percentile',
	'SAT_wr_75_percentile',

	'ACT_cumulative_MID',
	'ACT_cumulative_25_percentile',
	'ACT_cumulative_75_percentile',
	'ACT_eng_MID',
	'ACT_eng_25_percentile',
	'ACT_eng_75_percentile',
	'ACT_math_MID',
	'ACT_math_25_percentile',
	'ACT_math_75_percentile',
	'ACT_writing_MID',
	'ACT_writing_25_percentile',
	'ACT_writing_75_percentile',

	'Agriculture',
	'Natural_Resource',
	'Architecture',
	'Area_Ethnic_Cultural_Gender_Group_Studies',
	'Communication_Journalism',
	'Communication_Technologies',
	'Computer_Information_Sciences',
	'Personal_Culinary_Services',
	'Education',
	'Engineering',
	'Engineering_Technologies',
	'Foreign_Languages_Literatures_Linguistics',
	'Human_Sciences',
	'Legal_Professions_Studies',
	'English_Language_And_Literature',
	'General_Studies_And_Humanities',
	'Library_Science',
	'Biological_and_Biomedical_Sciences',
	'Mathematics_and_Statistics',
	'Military_Technologies_and_Applied_Sciences',
	'Interdiciplinary_Studies',
	'Parks_Recreation_Leisure_Fitness_Studies',
	'Philosophy_and_Religious_Studies',
	'Theology_and_Religious_Vocations',
	'Physical_Sciences',
	'Science_Technologies',
	'Psychology',
	'Homeland_Security_Law_Enforcement_Firefighting',
	'Public_Administration_and_Social_Service',
	'Social_Sciences',
	'Construction_Trade',
	'Mechanic_and_Repair_Technology',
	'Precision_Production',
	'Transportation_and_Materials_Moving',
	'Visual_and_Performing_Arts',
	'Health_Professions',
	'Business_Management_Marketing',
	'History',

	'enrollment',
	'percent_white',
	'percent_black',
	'percent_Hispanic',
	'percent_Asian',
	'percent_American_Indian',
	'percent_Native_Hawaiian',
	'percent_nonresident_aliens',

	'average_net_price_public_institutions',
	'average_net_price_private_institutions',

	'percent_student_of_Pell_Grant',
	'percent_student_of_Federal_Loan',

	'average_faculty_earnings']
state_list = [
	'state_id',
	'state_name',
	'state_abbreviation'
]

def _create_dictionary(keys, values):
	#assert len(keys) == len(values)
	returned_dict = {}
	for i in range (len(keys)):
		returned_dict[keys[i]] = values[i]
	return returned_dict

def get_connection():
	'''
	Returns a connection to the database described
	in the config module. Returns None if the
	connection attempt fails.
	'''
	connection = None
	try:
		connection = psycopg2.connect(database=config_johnny.database,
									  user=config_johnny.user,
									  password=config_johnny.password)
	except Exception as e:
		print(e, file=sys.stderr)
	return connection


@app.route('/')
def hello():
	return 'Hello, Users of Schoogle.'

@app.route('/schools')
def get_schools():
	#basic information:
	school_id = flask.request.args.get('school_id', default=None)
	school_name = flask.request.args.get('school_name', default=None)
	city = flask.request.args.get('city', default=None)
	state_id = flask.request.args.get('state_id', default=None)
	state_name = flask.request.args.get('state_name', default=None)
	highest_degree = flask.request.args.get('highest_degree', default=None)
	locale = flask.request.args.get('locale', default=None)
	ownership = flask.request.args.get('ownership', default=None)

	#Filters by test score
	SAT_average = flask.request.args.get('SAT_average', default=None)
	SAT_cr_MID = flask.request.args.get('SAT_cr_MID', default=None)
	SAT_cr_25_percentile = flask.request.args.get('SAT_cr_25_percentile', default=None)
	SAT_cr_75_percentile = flask.request.args.get('SAT_cr_75_percentile', default=None)
	SAT_math_MID = flask.request.args.get('SAT_math_MID', default=None)
	SAT_math_25_percentile = flask.request.args.get('SAT_math_25_percentile', default=None)
	SAT_math_75_percentile = flask.request.args.get('SAT_math_75_percentile', default=None)
	SAT_wr_MID = flask.request.args.get('SAT_wr_MID', default=None)
	SAT_wr_25_percentile = flask.request.args.get('SAT_wr_25_percentile', default=None)
	SAT_wr_75_percentile = flask.request.args.get('SAT_wr_75_percentile', default=None)


	ACT_cumulative_MID = flask.request.args.get('ACT_cumulative_MID', default=None)
	ACT_cumulative_25_percentile = flask.request.args.get('ACT_cumulative_25_percentile', default=None)
	ACT_cumulative_75_percentile = flask.request.args.get('ACT_cumulative_75_percentile', default=None)
	ACT_eng_MID = flask.request.args.get('ACT_eng_MID', default=None)
	ACT_eng_25_percentile = flask.request.args.get('ACT_eng_25_percentile', default=None)
	ACT_eng_75_percentile = flask.request.args.get('ACT_eng_75_percentile', default=None)
	ACT_math_MID = flask.request.args.get('ACT_math_MID', default=None)
	ACT_math_25_percentile = flask.request.args.get('ACT_math_25_percentile', default=None)
	ACT_math_75_percentile = flask.request.args.get('ACT_math_75_percentile', default=None)
	ACT_writing_MID = flask.request.args.get('ACT_writing_MID', default=None)
	ACT_writing_25_percentile = flask.request.args.get('ACT_writing_25_percentile', default=None)
	ACT_writing_75_percentile = flask.request.args.get('ACT_writing_75_percentile', default=None)

	#Filters by offering of specific majors
	Agriculture = flask.request.args.get('Agriculture', default=None)
	Natural_Resource = flask.request.args.get('Natural_Resource', default=None)
	Architecture = flask.request.args.get('Architecture', default=None)
	Area_Ethnic_Cultural_Gender_Group_Studies = flask.request.args.get('Area_Ethnic_Cultural_Gender_Group_Studies', default=None)
	Communication_Journalism = flask.request.args.get('Communication_Journalism', default=None)
	Communication_Technologies = flask.request.args.get('Communication_Technologies', default=None)
	Computer_Information_Sciences = flask.request.args.get('Computer_Information_Sciences', default=None)
	Personal_Culinary_Services = flask.request.args.get('Personal_Culinary_Services', default=None)
	Education = flask.request.args.get('Education', default=None)
	Engineering = flask.request.args.get('Engineering', default=None)
	Engineering_Technologies = flask.request.args.get('Engineering_Technologies', default=None)
	Foreign_Languages_Literatures_Linguistics = flask.request.args.get('Foreign_Languages_Literatures_Linguistics', default=None)
	Human_Sciences = flask.request.args.get('Human_Sciences', default=None)
	Legal_Professions_Studies = flask.request.args.get('Legal_Professions_Studies', default=None)
	English_Language_And_Literature = flask.request.args.get('English_Language_And_Literature', default=None)
	General_Studies_And_Humanities = flask.request.args.get('General_Studies_And_Humanities', default=None)
	Library_Science = flask.request.args.get('Library_Science', default=None)
	Biological_and_Biomedical_Sciences = flask.request.args.get('Biological_and_Biomedical_Sciences', default=None)
	Mathematics_and_Statistics = flask.request.args.get('Mathematics_and_Statistics', default=None)
	Military_Technologies_and_Applied_Sciences = flask.request.args.get('Military_Technologies_and_Applied_Sciences', default=None)
	Interdiciplinary_Studies = flask.request.args.get('Interdiciplinary_Studies', default=None)
	Parks_Recreation_Leisure_Fitness_Studies = flask.request.args.get('Parks_Recreation_Leisure_Fitness_Studies', default=None)
	Philosophy_and_Religious_Studies = flask.request.args.get('Philosophy_and_Religious_Studies', default=None)
	Theology_and_Religious_Vocations = flask.request.args.get('Theology_and_Religious_Vocations', default=None)
	Physical_Sciences = flask.request.args.get('Physical_Sciences', default=None)
	Science_Technologies = flask.request.args.get('Science_Technologies', default=None)
	Psychology = flask.request.args.get('Psychology', default=None)
	Homeland_Security_Law_Enforcement_Firefighting = flask.request.args.get('Homeland_Security_Law_Enforcement_Firefighting', default=None)
	Public_Administration_and_Social_Service = flask.request.args.get('Public_Administration_and_Social_Service', default=None)
	Social_Sciences = flask.request.args.get('Social_Sciences', default=None)
	Construction_Trade = flask.request.args.get('Construction_Trade', default=None)
	Mechanic_and_Repair_Technology = flask.request.args.get('Mechanic_and_Repair_Technology', default=None)
	Precision_Production = flask.request.args.get('Precision_Production', default=None)
	Transportation_and_Materials_Moving = flask.request.args.get('Transportation_and_Materials_Moving', default=None)
	Visual_and_Performing_Arts = flask.request.args.get('Visual_and_Performing_Arts', default=None)
	Health_Professions = flask.request.args.get('Health_Professions', default=None)
	Business_Management_Marketing = flask.request.args.get('Business_Management_Marketing', default=None)
	History = flask.request.args.get('History', default=None)


	admission_rate = flask.request.args.get('admission_rate', default=None)

	enrollment = flask.request.args.get('enrollment', default=None)
	percent_white = flask.request.args.get('percent_white', default=None)
	percent_black = flask.request.args.get('percent_black', default=None)
	percent_Hispanic = flask.request.args.get('percent_Hispanic', default=None)
	percent_Asian = flask.request.args.get('percent_Asian', default=None)
	percent_American_Indian = flask.request.args.get('percent_American_Indian', default=None)
	percent_Native_Hawaiian = flask.request.args.get('percent_Native_Hawaiian', default=None)
	percent_nonresident_aliens = flask.request.args.get('percent_nonresident_aliens', default=None)

	#Filters by misc other metrics
	average_net_price_public_institutions = flask.request.args.get('average_net_price_public_institutions', default=None)
	average_net_price_private_institutions = flask.request.args.get('average_net_price_private_institutions', default=None)
	percent_student_of_Pell_Grant = flask.request.args.get('percent_student_of_Pell_Grant', default=None)
	percent_student_of_Federal_Loan = flask.request.args.get('percent_student_of_Federal_Loan', default=None)
	average_faculty_earnings = flask.request.args.get('average_faculty_earnings', default=None)


	school_list = _get_all_school_stats() #All the schools to be filtered

	#Basic Information
	if school_id is not None:
		school_list = _filter_school_by_basics(school_list, school_id, 'school_id')
	if school_name is not None:
		school_list = _filter_school_by_basics(school_list, school_name, 'school_name')
	if city is not None:
		school_list = _filter_school_by_basics(school_list, city, 'city')
	if state_id is not None:
		school_list = _filter_school_by_basics(school_list, state_id, 'state_id')
	if state_name is not None:
		school_list = _filter_school_by_basics(school_list, state_name, 'state_name')
	if highest_degree is not None:
		school_list = _filter_school_by_basics(school_list, highest_degree, 'highest_degree')
	if locale is not None:
		school_list = _filter_school_by_basics(school_list, locale, 'locale')
	if ownership is not None:
		school_list = _filter_school_by_basics(school_list, ownership, 'ownership')

	#Majors
	if Agriculture == 'True': 
		school_list = _filter_school_by_major(school_list, 'Agriculture')
	if Natural_Resource == 'True':
		school_list = _filter_school_by_major(school_list, 'Natural_Resource')
	if Architecture == 'True':
		school_list = _filter_school_by_major(school_list, 'Architecture')
	if Area_Ethnic_Cultural_Gender_Group_Studies == 'True':
		school_list = _filter_school_by_major(school_list, 'Area_Ethnic_Cultural_Gender_Group_Studies')
	if Communication_Journalism == 'True':
		school_list = _filter_school_by_major(school_list, 'Communication_Journalism')
	if Communication_Technologies == 'True':
		school_list = _filter_school_by_major(school_list, 'Communication_Technologies')
	if Computer_Information_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Computer_Information_Sciences')
	if Personal_Culinary_Services == 'True':
		school_list = _filter_school_by_major(school_list, 'Personal_Culinary_Services')
	if Education == 'True':
		school_list = _filter_school_by_major(school_list, 'Education')
	if Engineering == 'True':
		school_list = _filter_school_by_major(school_list, 'Engineering')
	if Engineering_Technologies == 'True':
		school_list = _filter_school_by_major(school_list, 'Engineering_Technologies')
	if Foreign_Languages_Literatures_Linguistics == 'True':
		school_list = _filter_school_by_major(school_list, 'Foreign_Languages_Literatures_Linguistics')
	if Human_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Human_Sciences')
	if Legal_Professions_Studies == 'True':
		school_list = _filter_school_by_major(school_list, 'Legal_Professions_Studies')
	if English_Language_And_Literature == 'True':
		school_list = _filter_school_by_major(school_list, 'English_Language_And_Literature')
	if General_Studies_And_Humanities == 'True':
		school_list = _filter_school_by_major(school_list, 'General_Studies_And_Humanities')
	if Library_Science == 'True':
		school_list = _filter_school_by_major(school_list, 'Library_Science')
	if Biological_and_Biomedical_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Biological_and_Biomedical_Sciences')
	if Mathematics_and_Statistics == 'True':
		school_list = _filter_school_by_major(school_list, 'Mathematics_and_Statistics')
	if Military_Technologies_and_Applied_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Military_Technologies_and_Applied_Sciences')
	if Interdiciplinary_Studies == 'True':
		school_list = _filter_school_by_major(school_list, 'Interdiciplinary_Studies')
	if Parks_Recreation_Leisure_Fitness_Studies == 'True':
		school_list = _filter_school_by_major(school_list, 'Parks_Recreation_Leisure_Fitness_Studies')
	if Philosophy_and_Religious_Studies == 'True':
		school_list = _filter_school_by_major(school_list, 'Philosophy_and_Religious_Studies')
	if Theology_and_Religious_Vocations == 'True':
		school_list = _filter_school_by_major(school_list, 'Theology_and_Religious_Vocations')
	if Physical_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Physical_Sciences')
	if Science_Technologies == 'True':
		school_list = _filter_school_by_major(school_list, 'Science_Technologies')
	if Psychology == 'True':
		school_list = _filter_school_by_major(school_list, 'Psychology')
	if Homeland_Security_Law_Enforcement_Firefighting == 'True':
		school_list = _filter_school_by_major(school_list, 'Homeland_Security_Law_Enforcement_Firefighting')
	if Public_Administration_and_Social_Service == 'True':
		school_list = _filter_school_by_major(school_list, 'Public_Administration_and_Social_Service')
	if Social_Sciences == 'True':
		school_list = _filter_school_by_major(school_list, 'Social_Sciences')
	if Construction_Trade == 'True':
		school_list = _filter_school_by_major(school_list, 'Construction_Trade')
	if Mechanic_and_Repair_Technology == 'True':
		school_list = _filter_school_by_major(school_list, 'Mechanic_and_Repair_Technology')
	if Precision_Production == 'True':
		school_list = _filter_school_by_major(school_list, 'Precision_Production')
	if Transportation_and_Materials_Moving == 'True':
		school_list = _filter_school_by_major(school_list, 'Transportation_and_Materials_Moving')
	if Visual_and_Performing_Arts == 'True':
		school_list = _filter_school_by_major(school_list, 'Visual_and_Performing_Arts')
	if Health_Professions == 'True':
		school_list = _filter_school_by_major(school_list, 'Health_Professions')
	if Business_Management_Marketing == 'True':
		school_list = _filter_school_by_major(school_list, 'Business_Management_Marketing')
	if History == 'True':
		school_list = _filter_school_by_major(school_list, 'History')

	#number comparisons
	if SAT_average is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_average, 'SAT_average')
	if SAT_cr_MID is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_cr_MID, 'SAT_cr_MID')
	if SAT_cr_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_cr_25_percentile, 'SAT_cr_25_percentile')
	if SAT_cr_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_cr_75_percentile, 'SAT_cr_75_percentile')
	if SAT_math_MID is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_math_MID, 'SAT_math_MID')
	if SAT_math_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_math_25_percentile, 'SAT_math_25_percentile')
	if SAT_math_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_math_75_percentile, 'SAT_math_75_percentile')
	if SAT_wr_MID is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_wr_MID, 'SAT_wr_MID')
	if SAT_wr_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_wr_25_percentile, 'SAT_wr_25_percentile')
	if SAT_wr_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, SAT_wr_75_percentile, 'SAT_wr_75_percentile')
	if ACT_cumulative_MID is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_cumulative_MID, 'ACT_cumulative_MID')
	if ACT_cumulative_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_cumulative_25_percentile, 'ACT_cumulative_25_percentile')
	if ACT_cumulative_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_cumulative_75_percentile, 'ACT_cumulative_75_percentile')
	if ACT_eng_MID is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_eng_MID, 'ACT_eng_MID')
	if ACT_eng_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_eng_25_percentile, 'ACT_eng_25_percentile')
	if ACT_eng_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_eng_75_percentile, 'ACT_eng_75_percentile')
	if ACT_math_MID is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_math_MID, 'ACT_math_MID')
	if ACT_math_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_math_25_percentile, 'ACT_math_25_percentile')
	if ACT_math_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_math_75_percentile, 'ACT_math_75_percentile')
	if ACT_writing_MID is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_writing_MID, 'ACT_writing_MID')
	if ACT_writing_25_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_writing_25_percentile, 'ACT_writing_25_percentile')
	if ACT_writing_75_percentile is not None:
		school_list = _filter_school_by_number_range(school_list, ACT_writing_75_percentile, 'ACT_writing_75_percentile')

	if admission_rate is not None:
		school_list = _filter_school_by_number_range(school_list, admission_rate, 'admission_rate')

	if enrollment is not None:
		school_list = _filter_school_by_number_range(school_list, enrollment, 'enrollment')
	if percent_white is not None:
		school_list = _filter_school_by_number_range(school_list, percent_white, 'percent_white')
	if percent_black is not None:
		school_list = _filter_school_by_number_range(school_list, percent_black, 'percent_black')
	if percent_Hispanic is not None:
		school_list = _filter_school_by_number_range(school_list, percent_Hispanic, 'percent_Hispanic')
	if percent_Asian is not None:
		school_list = _filter_school_by_number_range(school_list, percent_Asian, 'percent_Asian')
	if percent_American_Indian is not None:
		school_list = _filter_school_by_number_range(school_list, percent_American_Indian, 'percent_American_Indian')
	if percent_nonresident_aliens is not None:
		school_list = _filter_school_by_number_range(school_list, percent_nonresident_aliens, 'percent_nonresident_aliens')
	if average_net_price_public_institutions is not None:
		school_list = _filter_school_by_number_range(school_list, average_net_price_public_institutions, 'average_net_price_public_institutions')
	if average_net_price_private_institutions is not None:
		school_list = _filter_school_by_number_range(school_list, average_net_price_private_institutions, 'average_net_price_private_institutions')
	if percent_student_of_Pell_Grant is not None:
		school_list = _filter_school_by_number_range(school_list, percent_student_of_Pell_Grant, 'percent_student_of_Pell_Grant')
	if percent_student_of_Federal_Loan is not None:
		school_list = _filter_school_by_number_range(school_list, percent_student_of_Federal_Loan, 'percent_student_of_Federal_Loan')
	if average_faculty_earnings is not None:
		school_list = _filter_school_by_number_range(school_list, average_faculty_earnings, 'average_faculty_earnings')


	return json.dumps(school_list)




def _get_all_schools_basics():
	connection = get_connection()
	try:
		cursor = connection.cursor()
		query = '''SELECT school_id ,school_name, city,state_name,school_url,highest_degree,locale,ownership 
					FROM schools, states 
					WHERE schools.state_id = states.state_id'''
		cursor.execute(query)
	except Exception as e:
		print(e)
		exit()

	schools = []
	for row in cursor:
		schools.append(_create_dictionary(basic_list,row))
	connection.close()
	return schools

def _get_all_school_stats():
	connection = get_connection()
	try:
		cursor = connection.cursor()
		query = '''SELECT * 
					FROM schools, school_stats, states 
					WHERE schools.state_id = states.state_id
					AND schools.school_id = school_stats.school_id'''
		cursor.execute(query)
	except Exception as e:
		print(e)
		exit()

	school_stats = []
	for row in cursor:
		school_stats.append(_create_dictionary(basic_list+stats_list+state_list,row))
	connection.close()
	return school_stats

def __cast_int(num):
	if num == '':
		return None
	try:
		return int(num)
	except:
		return __cast_float(num)
def __cast_float(num):
	try:
		return float(num)
	except Exception as e:
		raise e
		print(e)
		quit()
def __get_min_max(input):
	#The maximum int psql stored is 2147483647
	min_and_max = {'min': -1, 'max': 2147483647}
	for i in range(len(input)):
		if i > 0 and input[i] == '.' and input[i-1] =='.':
			if input[:i-1] != '':
				try:
					min_and_max['min'] = __cast_int(input[:i-1])
				except Exception as e:
					raise ValueError('must be numeric range')
			if input[i+1:] != '':
				try:
					min_and_max['max'] = __cast_int(input[i+1:])
				except Exception as e:
					raise ValueError('must be numeric range')
	return min_and_max

def _filter_school_by_basics(school_list, metric_value, metric_name):
	school_index = 0
	while school_index < len(school_list):
		if(str(metric_value).lower() not in str(school_list[school_index][metric_name]).lower()):
			school_list.remove(school_list[school_index])
			school_index -= 1
		school_index += 1
	return school_list

def _filter_school_by_number_range(school_list, metric_value, metric_name):
	school_index = 0
	range_dict = __get_min_max(metric_value)
	while school_index < len(school_list):
		if school_list[school_index][metric_name] is not None:
			if (str(school_list[school_index][metric_name]) == "null" or school_list[school_index][metric_name] < range_dict['min'] or school_list[school_index][metric_name] > range_dict['max']):
				school_list.remove(school_list[school_index])
				school_index -= 1
		else:
			school_list.remove(school_list[school_index])
			school_index -= 1
		school_index += 1
	return school_list

def _filter_school_by_major(school_list, major):
	#In filtering, python shifts the list if an entry is removed
	#to account for the shift, we use tricks (I mean the -=1 and +=1)
	school_index = 0
	while school_index < len(school_list):
		if (school_list[school_index][major] == False):			
			school_list.remove(school_list[school_index])
			school_index -= 1
		school_index += 1
	return school_list

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host port'.format(sys.argv[0]))
		print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
		exit()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	app.run(host=host, port=port, debug=True)

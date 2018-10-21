'''
10/19/2018 school_data_converter
'''
import sys
import re
import csv


#Assigned state ID matched to state name
state_match = {
'1': 'Alabama',
'2': 'Alaska',
'4': 'Arizona',
'5': 'Arkansas',
'6': 'California',
'8': 'Colorado',
'9': 'Connecticut',
'10': 'Delaware',
'11': 'District of Columbia',
'12': 'Florida',
'13': 'Georgia',
'15': 'Hawaii',
'16': 'Idaho',
'17': 'Illinois',
'18': 'Indiana',
'19': 'Iowa',
'20': 'Kansas',
'21': 'Kentucky',
'22': 'Louisiana',
'23': 'Maine',
'24': 'Maryland',
'25': 'Massachusetts',
'26': 'Michigan',
'27': 'Minnesota',
'28': 'Mississippi',
'29': 'Missouri',
'30': 'Montana',
'31': 'Nebraska',
'32': 'Nevada',
'33': 'New Hampshire',
'34': 'New Jersey',
'35': 'New Mexico',
'36': 'New York',
'37': 'North Carolina',
'38': 'North Dakota',
'39': 'Ohio',
'40': 'Oklahoma',
'41': 'Oregon',
'42': 'Pennsylvania',
'44': 'Rhode Island',
'45': 'South Carolina',
'46': 'South Dakota',
'47': 'Tennessee',
'48': 'Texas',
'49': 'Utah',
'50': 'Vermont',
'51': 'Virginia',
'53': 'Washington',
'54': 'West Virginia',
'55': 'Wisconsin',
'56': 'Wyoming',
'60': 'American Samoa',
'64': 'Federated States of Micronesia',
'66': 'Guam',
'68': 'Marshal Islands',
'69': 'Northern Mariana Islands',
'70': 'Palau',
'72': 'Puerto Rico',
'78': 'Virgin Islands',
'ST_FIPS': 'State Name'
}
#Convert the major offered in INT expression to BOOLEAN expression
def _convert_int_to_boolean(value):
	if value == '0': #Program not offered
		return False
	else: #Program offered
		return True

#Convert highest degree/locale/ownership to English text
def _convert_int_to_text(metric, value):
	if metric == 'highest_degree':
		if value == '0':
			return 'Non-degree-granting'
		elif value == '1':
			return 'Certificate degree'
		elif value == '2':
			return 'Associate degree'
		elif value == '3':
			return 'Bachelor\'s degree'
		elif value == '4':
			return 'Graduate degree'
		elif value == 'NULL':
			return 'NULL'
		else:
			return 'illegal'

	elif metric == 'locale':
		if value == '11':
			return 'City: Large'
		elif value == '12':
			return 'City: Midsize'
		elif value == '13':
			return 'City: Small'
		elif value == '21':
			return 'Suburb: Large'
		elif value == '22':
			return 'Suburb: Midsize'
		elif value == '23':
			return 'Suburb: Small'
		elif value == '31':
			return 'Town: Fringe'
		elif value == '32':
			return 'Town: Distant'
		elif value == '33':
			return 'Town: Remote'
		elif value == '41':
			return 'Rural: Fringe'
		elif value == '42':
			return 'Rural: Distant'
		elif value == '43':
			return 'Rural: Remote'
		elif value == 'NULL':
			return 'NULL'
		else:
			return 'locale unknown'

	elif metric == 'ownership':
		if value == '1':
			return 'Public'
		elif value == '2':
			return 'Private nonprofit'
		elif value == '3':
			return 'Private for-profit'
		elif value == 'NULL':
			return 'NULL'
		else:
			return 'unknown ownership'
#Checking if the school stats information is null
def float_stats_null_checker(value):
	if value == 'NULL':
		return 'NULL'
	else:
		return float(value)
def int_stats_null_checker(value):
	if value == 'NULL':
		return 'NULL'
	else:
		return int(value)

def load_school(csv_file_name):
	#column1(UNITID) is INT school ID
	#column4(INSTNM) is TEXT school name
	#column5(CITY) is TEXT city
	#column18(ST_FIPS) is INT state ID,
	#column9(INSTURL) is TEXT school_url
	#column16(HIGHDEG) is INT highest_degree, CONVERTE TO TEXT!!!
	#column20(LOCALE) is INT locale, CONVERTE TO TEXT!!!
	#column17(CONTROL) is INT ownership, CONVERTE TO TEXT!!!
	csv_file = open(csv_file_name, encoding='utf-8-sig')
	reader = csv.reader(csv_file)

	schools = []
	school = {}
	for row in reader:
		school = {
		'school_id': int(row[0]),
		'school_name': row[3],
		'city': row[4],
		'state_id': row[17],
		'school_url': row[8],
		'highest_degree': _convert_int_to_text('highest_degree', row[15]),
		'locale':  _convert_int_to_text('locale', row[19]),
		'ownership': _convert_int_to_text('ownership', row[16])
		}
		schools.append(school)
	csv_file.close()
	return schools

def load_school_stats(csv_file_name):
	csv_file = open(csv_file_name, encoding='utf-8-sig')
	reader = csv.reader(csv_file)

	schools_stats = []
	stats = {}
	for row in reader:
		assert len(row) == 1847
		stats = {
		'school_id': int(row[0]),
		'year': 2016,
		'admission_rate': float_stats_null_checker(row[37-1]),

		#SAT:
		'SAT_average': float_stats_null_checker(row[60-1]),
		'SAT_cr_MID': float_stats_null_checker(row[45-1]),
		'SAT_cr_25_percentile': float_stats_null_checker(row[39-1]),
		'SAT_cr_75_percentile': float_stats_null_checker(row[40-1]),
		'SAT_math_MID': float_stats_null_checker(row[46-1]),
		'SAT_math_25_percentile': float_stats_null_checker(row[41-1]),
		'SAT_math_75_percentile': float_stats_null_checker(row[42-1]),
		'SAT_wr_MID': float_stats_null_checker(row[47-1]),
		'SAT_wr_25_percentile': float_stats_null_checker(row[43-1]),
		'SAT_wr_75_percentile': float_stats_null_checker(row[44-1]),

		#ACT:
		'ACT_cumulative_MID': float_stats_null_checker(row[56-1]),
		'ACT_cumulative_25_percentile': float_stats_null_checker(row[48-1]),
		'ACT_cumulative_75_percentile': float_stats_null_checker(row[49-1]),
		'ACT_eng_MID': float_stats_null_checker(row[57-1]),
		'ACT_eng_25_percentile': float_stats_null_checker(row[50-1]),
		'ACT_eng_75_percentile': float_stats_null_checker(row[51-1]),
		'ACT_math_MID': float_stats_null_checker(row[58-1]),
		'ACT_math_25_percentile': float_stats_null_checker(row[52-1]),
		'ACT_math_75_percentile': float_stats_null_checker(row[53-1]),
		'ACT_writing_MID': float_stats_null_checker(row[59-1]),
		'ACT_writing_25_percentile': float_stats_null_checker(row[54-1]),
		'ACT_writing_75_percentile': float_stats_null_checker(row[55-1]),

		#Academics:
		'Agriculture': _convert_int_to_boolean(row[104-1]),
		'Natural_Resource': _convert_int_to_boolean(row[109-1]),
		'Architecture': _convert_int_to_boolean(row[114-1]),
		'Area_Ethnic_Cultural_Gender_Group_Studies': _convert_int_to_boolean(row[119-1]),
		'Communication_Journalism': _convert_int_to_boolean(row[124-1]),
		'Communication_Technologies': _convert_int_to_boolean(row[129-1]),
		'Computer_Information_Sciences': _convert_int_to_boolean(row[134-1]),
		'Personal_Culinary_Services': _convert_int_to_boolean(row[139-1]),
		'Education': _convert_int_to_boolean(row[144-1]),
		'Engineering': _convert_int_to_boolean(row[149-1]),
		'Engineering_Technologies': _convert_int_to_boolean(row[154-1]),
		'Foreign_Languages_Literatures_Linguistics': _convert_int_to_boolean(row[159-1]),
		'Human_Sciences': _convert_int_to_boolean(row[164-1]),
		'Legal_Professions_Studies': _convert_int_to_boolean(row[169-1]),
		'English_Language_And_Literature': _convert_int_to_boolean(row[174-1]),
		'General_Studies_And_Humanities': _convert_int_to_boolean(row[179-1]),
		'Library_Science': _convert_int_to_boolean(row[184-1]),
		'Biological_and_Biomedical_Sciences': _convert_int_to_boolean(row[189-1]),
		'Mathematics_and_Statistics': _convert_int_to_boolean(row[194-1]),
		'Military_Technologies_and_Applied_Sciences': _convert_int_to_boolean(row[199-1]),
		'Interdiciplinary_Studies': _convert_int_to_boolean(row[204-1]),
		'Parks_Recreation_Leisure_Fitness_Studies': _convert_int_to_boolean(row[209-1]),
		'Philosophy_and_Religious_Studies': _convert_int_to_boolean(row[214-1]),
		'Theology_and_Religious_Vocations': _convert_int_to_boolean(row[219-1]),
		'Physical_Sciences': _convert_int_to_boolean(row[224-1]),
		'Science_Technologies': _convert_int_to_boolean(row[229-1]),
		'Psychology': _convert_int_to_boolean(row[234-1]),
		'Homeland_Security_Law_Enforcement_Firefighting': _convert_int_to_boolean(row[239-1]),
		'Public_Administration_and_Social_Service': _convert_int_to_boolean(row[244-1]),
		'Social_Sciences': _convert_int_to_boolean(row[249-1]),
		'Construction_Trade': _convert_int_to_boolean(row[254-1]),
		'Mechanic_and_Repair_Technology': _convert_int_to_boolean(row[259-1]),
		'Precision_Production': _convert_int_to_boolean(row[264-1]),
		'Transportation_and_Materials_Moving': _convert_int_to_boolean(row[269-1]),
		'Visual_and_Performing_Arts': _convert_int_to_boolean(row[274-1]),
		'Health_Professions': _convert_int_to_boolean(row[279-1]),
		'Business_Management_Marketing': _convert_int_to_boolean(row[284-1]),
		'History': _convert_int_to_boolean(row[289-1]),

		#Student Body: (Didn't find information about age)
		'enrollment': int_stats_null_checker(row[290]),
		'percent_white': float_stats_null_checker(row[292]),
		'percent_black': float_stats_null_checker(row[293]),
		'percent_Hispanic': float_stats_null_checker(row[294]),
		'percent_Asian': float_stats_null_checker(row[295]),
		'percent_American_Indian': float_stats_null_checker(row[296]),
		'percent_Native_Hawaiian': float_stats_null_checker(row[297]),
		'percent_nonresident_aliens': float_stats_null_checker(row[299]),

		#Cost & Earnings:
		'average_net_price_public_institutions': int_stats_null_checker(row[316]),
		'average_net_price_private_institutions': int_stats_null_checker(row[317]),

		'percent_student_of_Pell_Grant': float_stats_null_checker(row[385]),
		'percent_student_of_Federal_Loan': float_stats_null_checker(row[437]),

		'average_faculty_earnings': int_stats_null_checker(row[383])
		}
		schools_stats.append(stats)
	csv_file.close()
	return schools_stats
def load_state(csv_file_name, encoding='utf-8-sig'):
	csv_file = open(csv_file_name)
	reader = csv.reader(csv_file)

	states = []
	state = {}
	for row in reader:
		assert len(row) == 1847
		state = {
		'state_id': row[17],
		'state_name': state_match[row[17]],
		'state_abbreviation': row[5],
		}
		states.append(state)
	csv_file.close()
	return states


def save_schools_table(schools, csv_file_name):
    ''' Save the schools in CSV form, with each row containing
        (school_id, school_name, city, state_id, school_url, highest_degree, locale, ownership). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for school in schools:
        school_row = [	school['school_id'],
        				school['school_name'],
        				school['city'],
        				school['state_id'],
        				school['school_url'],
        				school['highest_degree'],
        				school['locale'],
        				school['ownership']]
        writer.writerow(school_row)
    output_file.close()

def save_school_stats_table(school_stats, csv_file_name):
    ''' Save the school_stats in CSV form, with each row containing the following
    '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for stats in school_stats:
        school_stats_row = [stats['school_id'],
							stats['year'],
							stats['admission_rate'],
		#SAT:
							stats['SAT_average'],
							stats['SAT_cr_MID'],
							stats['SAT_cr_25_percentile'],
							stats['SAT_cr_75_percentile'],
							stats['SAT_math_MID'],
							stats['SAT_math_25_percentile'],
							stats['SAT_math_75_percentile'],
							stats['SAT_wr_MID'],
							stats['SAT_wr_25_percentile'],
							stats['SAT_wr_75_percentile'],
		#ACT:
							stats['ACT_cumulative_MID'],
							stats['ACT_cumulative_25_percentile'],
							stats['ACT_cumulative_75_percentile'],
							stats['ACT_eng_MID'],
							stats['ACT_eng_25_percentile'],
							stats['ACT_eng_75_percentile'],
							stats['ACT_math_MID'],
							stats['ACT_math_25_percentile'],
							stats['ACT_math_75_percentile'],
							stats['ACT_writing_MID'],
							stats['ACT_writing_25_percentile'],
							stats['ACT_writing_75_percentile'],
		#Academics:
							stats['Agriculture'],
							stats['Natural_Resource'],
							stats['Architecture'],
							stats['Area_Ethnic_Cultural_Gender_Group_Studies'],
							stats['Communication_Journalism'],
							stats['Communication_Technologies'],
							stats['Computer_Information_Sciences'],
							stats['Personal_Culinary_Services'],
							stats['Education'],
							stats['Engineering'],
							stats['Engineering_Technologies'],
							stats['Foreign_Languages_Literatures_Linguistics'],
							stats['Human_Sciences'],
							stats['Legal_Professions_Studies'],
							stats['English_Language_And_Literature'],
							stats['General_Studies_And_Humanities'],
							stats['Library_Science'],
							stats['Biological_and_Biomedical_Sciences'],
							stats['Mathematics_and_Statistics'],
							stats['Military_Technologies_and_Applied_Sciences'],
							stats['Interdiciplinary_Studies'],
							stats['Parks_Recreation_Leisure_Fitness_Studies'],
							stats['Philosophy_and_Religious_Studies'],
							stats['Theology_and_Religious_Vocations'],
							stats['Physical_Sciences'],
							stats['Science_Technologies'],
							stats['Psychology'],
							stats['Homeland_Security_Law_Enforcement_Firefighting'],
							stats['Public_Administration_and_Social_Service'],
							stats['Social_Sciences'],
							stats['Construction_Trade'],
							stats['Mechanic_and_Repair_Technology'],
							stats['Precision_Production'],
							stats['Transportation_and_Materials_Moving'],
							stats['Visual_and_Performing_Arts'],
							stats['Health_Professions'],
							stats['Business_Management_Marketing'],
							stats['History'],
		#Student Body: (Didn't find information about age)
							stats['enrollment'],
							stats['percent_white'],
							stats['percent_black'],
							stats['percent_Hispanic'],
							stats['percent_Asian'],
							stats['percent_American_Indian'],
							stats['percent_Native_Hawaiian'],
							stats['percent_nonresident_aliens'],
		#Cost & Earnings:
							stats['average_net_price_public_institutions'],
							stats['average_net_price_private_institutions'],

							stats['percent_student_of_Pell_Grant'],
							stats['percent_student_of_Federal_Loan'],

							stats['average_faculty_earnings']]
        writer.writerow(school_stats_row)
    output_file.close()

def save_states_table(states, csv_file_name):
    ''' Save the states in CSV form, with each row containing
        (state id, state name, and state abbreviation). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for state in states:
        state_row = [	state['state_id'],
        				state['state_name'],
        				state['state_abbreviation']]
        writer.writerow(state_row)
    output_file.close()

def main():
	save_schools_table(load_school('MERGED2016_17_PP.csv'), 'schools.csv')
	save_school_stats_table(load_school_stats('MERGED2016_17_PP.csv'), 'school_stats.csv')
	save_states_table(load_state('MERGED2016_17_PP.csv'),'states.csv')

if __name__ == '__main__':
	main()
	# books, authors, books_authors = load_from_books_csv_file('books-original.csv')

	# save_books_table(books, 'books.csv')
	# save_authors_table(authors, 'authors.csv')
	# save_linking_table(books_authors, 'books_authors.csv')




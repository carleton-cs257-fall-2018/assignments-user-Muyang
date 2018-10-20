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

#Convert highest degree/locale/ownership to English text
def convert_int_to_text(metric, value):
	if metric == 'highest_degree':
		if value == 0:
			return 'Non-degree-granting'
		elif value == 1:
			return 'Certificate degree'
		elif value == 2:
			return 'Associate degree'
		elif value == 3:
			return 'Bachelor\'s degree'
		elif value == 4:
			return 'Graduate degree'
		else:
			return 'unkown highest degree'

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
		else:
			return 'locale unkown'

	elif metric == 'ownership':
		if value == '1':
			return 'Public'
		elif value == '2':
			return 'Private nonprofit'
		elif value == '3':
			return 'Private for-profit'
		else:
			return 'unkown ownership'


def load_school(csv_file_name):
	#column1(UNITID) is INT school ID
	#column4(INSTNM) is TEXT school name
	#column5(CITY) is TEXT city
	#column18(ST_FIPS) is INT state ID,
	#column9(INSTURL) is TEXT school_url
	#column16(HIGHDEG) is INT highest_degree, CONVERTE TO TEXT!!!
	#column20(LOCALE) is INT locale, CONVERTE TO TEXT!!!
	#column17(CONTROL) is INT ownership, CONVERTE TO TEXT!!!
	csv_file = open(csv_file_name)
	reader = csv.reader(csv_file)

	schools = []
	school = {}
	for row in reader:
		assert len(row) == 1847
		school = {
		'school_id': row[0],
		'school_name': row[3],
		'city': row[4],
		'state_id': row[17],
		'school_url': row[8],
		'highest_degree': convert_int_to_text('higest_degree', row[15]),
		'locale':  convert_int_to_text('locale', row[19]),
		'ownership': convert_int_to_text('ownership', row[16])
		}
		schools.append(school)
	csv_file.close()
	return schools

def load_school_stats(csv_file_name):
	csv_file = open(csv_file_name)
	reader = csv.reader(csv_file)

	schools_stats = []
	stats = {}
	for row in reader:
		assert len(row) == 1847
		stats = {
		'school_id': row[0],
		'year': 2016,
		'admission_rate': row[37],

		#SAT:
		'SAT_average': row[60],
		'SAT_cr_MID': row[45],
		'SAT_cr_25_percentile': row[39],
		'SAT_cr_75_percentile': row[40],
		'SAT_math_MID': row[46],
		'SAT_math_25_percentile': row[41],
		'SAT_math_75_percentile': row[42],
		'SAT_wr_MID': row[47],
		'SAT_wr_25_percentile': row[43],
		'SAT_wr_75_percentile': row[44],

		#ACT:
		'ACT_cumulative_MID': row[56],
		'ACT_cumulative_25_percentile': row[48],
		'ACT_cumulative_75_percentile': row[49],
		'ACT_eng_MID': row[57],
		'ACT_eng_25_percentile': row[50],
		'ACT_eng_75_percentile': row[51],
		'ACT_math_MID': row[58],
		'ACT_math_25_percentile': row[52],
		'ACT_math_75_percentile': row[53],
		'ACT_writing_MID': row[59],
		'ACT_writing_25_percentile': row[54],
		'ACT_writing_75_percentile': row[55],

		#Academics:
		'Agriculture': row[],
		'Natural_Resource': row[],
		'Architecture': row[],
		'Area_Ethnic_Cultural_Gender_Group_Studies': row[],
		'Communication_Journalism': row[],
		'Communication_Technologies': row[],
		'Computer_Information_Sciences': row[],
		'Personal_Culinary_Services': row[],
		'Education': row[],
		'Engineering': row[],
		'Engineering_Technologies': row[]
		'Foreign_Languages_Literatures_Linguistics': row[],
		'Human_Sciences': row[],
		'Legal_Professions_Studies': row[],
		'English_Language_And_Literature': row[],
		'General_Studies_And_Humanities': row[],
		'Library_Science': row[],
		'Biological_and_Biomedical_Sciences': row[],
		'Mathematics_and_Statistics': row[],
		'Military_Technologies_and_Applied_Sciences': row[],
		'Interdiciplinary_Studies': row[],
		'Parks_Recreation_Leisure_Fitness_Studies': row[],
		'Philosophy_and_Religious_Studies': row[],
		'Theology_and_Religious_Vocations': row[]
		'Physical_Sciences': row[],
		'Science_Technologies': row[],
		'Psychology': row[],
		'Homeland_Security_Law_Enforcement_Firefighting': row[],
		'Public_Administration_and_Social_Service': row[],
		'Social_Sciences': row[],
		'Construction_Trade': row[],
		'Mechanic_and_Repair_Technology': row[],
		'Precision_Production': row[],
		'Transportation_and_Materials_Moving': row[],
		'Visual_and_Performing_Arts': row[],
		'Health_Professions': row[],
		'Business_Management_Marketing': row[],
		'History': row[],

		#Student Body: (Didn't find information about age)
		'enrollment' INT
		'percent_white' FLOAT,
		'percent_black' FLOAT,
		'percent_Hispanic' FLOAT,
		'percent_Asian' FLOAT,
		'percent_American_Indian' FLOAT,
		'percent_Native_Hawaiian' FLOAT,
		'percent_nonresident_aliens' FLOAT
		'percent_aged_25'+ FLOAT,

		#Cost & Earnings:
		'average_net_price_public_institutions' INT,
		'average_net_price_private_institutions' INT,

		'percent_student_of_Pell_Grant' FLOAT,
		'percent_student_of_Federal_Loan' FLOAT,

		'median_earning_6_years_after_entry' INT,
		'median_earning_8_years_after_entry' INT,
		'median_earning_10_years_after_entry' INT,

		'mean_earning_6_years_after_entry' INT,
		'mean_earning_8_years_after_entry' INT,
		'mean_earning_10_years_after_entry' INT,
		'standard_deviation_earnings_6_years_after_entry' FLOAT,
		'standard_deviation_earnings_8_years_after_entry' FLOAT,
		'standard_deviation_earnings_10_years_after_entry' FLOAT,

		'10th_percentile_earnings_6_years_after_entry' INT,
		'25th_percentile_earnings_6_years_after_entry' INT,
		'75th_percentile_earnings_6_years_after_entry' INT,
		'90th_percentile_earnings_6_years_after_entry' INT,

		'10th_percentile_earnings_8_years_after_entry' INT,
		'25th_percentile_earnings_8_years_after_entry' INT,
		'75th_percentile_earnings_8_years_after_entry' INT,
		'90th_percentile_earnings_8_years_after_entry' INT,

		'10th_percentile_earnings_10_years_after_entry' INT,
		'25th_percentile_earnings_10_years_after_entry' INT,
		'75th_percentile_earnings_10_years_after_entry' INT,
		'90th_percentile_earnings_10_years_after_entry' INT,

		'average_faculty_earnings' INT
		}
		schools_stats.append(stats)
	csv_file.close()
	return schools_stats
def load_state(csv_file_name):
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

def main():
	print(load_state('MERGED2016_17_PP.csv'))



if __name__ == '__main__':
	main()
	# books, authors, books_authors = load_from_books_csv_file('books-original.csv')

	# save_books_table(books, 'books.csv')
	# save_authors_table(authors, 'authors.csv')
	# save_linking_table(books_authors, 'books_authors.csv')




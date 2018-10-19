'''
10/19/2018 school_data_converter
'''
import sys
import re
import csv


def convert_int_text(metric, value):
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
		'id': row[0],
		'name': row[3],
		'city': row[4],
		'state_id': row[17],
		'school_url': row[8],
		'highest_degree': convert_int_text('higest_degree', row[15]),
		'locale':  convert_int_text('locale', row[19]),
		'ownership': convert_int_text('ownership', row[16])
		}
		schools.append(school)
	csv_file.close()
	return schools

def load_school_stats(csv_file_name):
	pass
def load_state(csv_file_name):
	pass
	#column18(ST_FIPS) is INT state ID, then add abbreviation and full name

def main():
	print(load_school('MERGED2016_17_PP.csv'))


if __name__ == '__main__':
	main()
	# books, authors, books_authors = load_from_books_csv_file('books-original.csv')

	# save_books_table(books, 'books.csv')
	# save_authors_table(authors, 'authors.csv')
	# save_linking_table(books_authors, 'books_authors.csv')
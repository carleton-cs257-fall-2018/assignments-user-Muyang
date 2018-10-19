'''
10/19/2018 school_data_converter
'''
import sys
import re
import csv

class Converter:

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



	def load_school_stats(csv_file_name):

	def load_state(csv_file_name):
		#column18(ST_FIPS) is INT state ID, then add abbreviation and full name

	if __name__ == '__main__':
    books, authors, books_authors = load_from_books_csv_file('books-original.csv')

    save_books_table(books, 'books.csv')
    save_authors_table(authors, 'authors.csv')
    save_linking_table(books_authors, 'books_authors.csv')
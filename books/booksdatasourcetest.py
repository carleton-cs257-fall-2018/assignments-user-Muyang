'''
	booksdatasourcetest.py
	Muyang Shi, Justin T. Washington, Chae Kim 18 Sept 2018
'''

import booksdatasource
import unittest

class booksdatasourcetest(unittest.TestCase):
	def setUp(self):
		self.books_data_source = booksdatasource.BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')
	def tearDown(self):
		pass

	#Testing the book(self, book_id) method
	def test_book(self):
		self.assertEqual(self.books_data_source.book(41),
			{'id':41,'title':'Middlemarch','publication-year':1871})
		self.assertEqual(self.books_data_source.book(5),
			{'id':5, 'title': 'Emma', 'publication-year': 1815})
	def test_book_no_id(self):
		self.assertRaises(ValueError, self.books_data_source.book, -1)

	#Testing the books method
	def test_books_author_id(self):
		self.assertEqual(self.books_data_source.books(author_id=22),
			[{'id':41, 'title':'Middlemarch','publication-year':1871},
			{'id':42, 'title':'Silas Marner', 'publication-year':1861 }])
		self.assertEqual(self.books_data_source.books(author_id=4),
			[{'id':5, 'title': 'Emma', 'publication-year': 1815},
			{'id':18, 'title': 'Pride and Prejudice', 'publication-year': 1813},
			{'id':20, 'title': 'Sense and Sensibility', 'publication-year': 1813}])

		self.assertEqual(self.books_data_source.books(author_id=16),
			[{'id':30, 'title':'1Q84', 'publication-year':2009},
			{'id':31, 'title':'A Wild Sheep Chase', 'publication-year':1982},
			{'id':32, 'title':'Hard-Boiled Wonderland and the End of the World', 'publication-year':1985}])

	def test_books_wrong_author_id(self):
		self.assertRaises(ValueError,self.books_data_source.books, author_id=-1)


	def test_books_search_text(self):
		self.assertEqual(self.books_data_source.books(search_text='middle'),
			[{'id':41, 'title':'Middlemarch','publication-year':1871}])

	def test_books_start_year(self):
		self.assertEqual(self.books_data_source.books(start_year=2016),
			[{'id':35, 'title':'The Power', 'publication-year':2016}])
	def test_books_wrong_start_year(self):
		self.assertRaises(ValueError, self.books_data_source.books, start_year='wrong')

	def test_books_end_year(self):
		self.assertEqual(self.books_data_source.books(end_year=1814),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])
	def test_books_wrong_end_year(self):
		self.assertRaises(ValueError,self.books_data_source.books,end_year='wrong')

	def test_books_author_id_with_start_year(self):
		self.assertEqual(self.books_data_source.books(start_year=1815, author_id=4 ),
			[{'id':5, 'title':'Emma', 'publication-year':1815}])
			#{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			#{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])
		self.assertEqual(self.books_data_source.books(author_id=16, start_year=1983),
			[{'id':30, 'title':'1Q84', 'publication-year':2009},
			{'id':32, 'title':'Hard-Boiled Wonderland and the End of the World', 'publication-year':1985}])
	def test_books_author_id_with_end_year(self):
		self.assertEqual(self.books_data_source.books(author_id=4, end_year=1817),
			[{'id':5, 'title':'Emma', 'publication-year':1815},
			{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])

	def test_books_search_text_with_start_year(self):
		self.assertEqual(self.books_data_source.books(search_text='THE', start_year=2016),
			[{'id':35, 'title':'The Power','publication-year':2016}])
	def test_books_search_text_with_end_year(self):
		self.assertEqual(self.books_data_source.books(end_year=1830,search_text='AND'),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])

	def test_books_sort_by_year(self):
		self.assertEqual(self.books_data_source.books(sort_by='year', author_id=4),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813},
			{'id':5, 'title':'Emma', 'publication-year':1815}])
	def test_books_sort_by_default(self):
		self.assertEqual(self.books_data_source.books(sort_by='whatsoever', author_id=4),
			[{'id':5, 'title':'Emma', 'publication-year':1815},
			{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])


	#Testing the books_for_author method
	def test_books_for_author(self):
		self.assertEqual(self.books_data_source.books_for_author(22),
			[{'id':41, 'title':'Middlemarch', 'publication-year':1871},
			 {'id':42, 'title':'Silas Marner', 'publication-year':1861}])

	def test_books_for_author_wrong_id(self):
		self.assertRaises(ValueError,self.books_data_source.books_for_author, -1)

	def test_author(self):
		self.assertEqual(self.books_data_source.author(22),
		{'id':22,'last-name':'Eliot','first-name':'George',
		'birth-year':1819,'death-year':1880})

	def test_authors_book_id(self):
		self.assertEqual(self.books_data_source.authors(book_id=41),
		[{"id":22, "last-name":"Eliot","first-name":"George",
		"birth-year":1819,"death-year":1880}])

	def test_authors_search_text(self):
		self.assertEqual(self.books_data_source.authors(search_text="je"),
		[{'id':21, 'last-name':'Jerome', 'first-name':'Jerome K.',
		'birth-year':1859, 'death-year': 1927},
		{'id':20, 'last-name':'Jemisen', 'first-name':'N.K.',
		'birth-year':1972, 'death-year': None}])

	def test_authors_start_year(self):
		self.assertEqual(self.books_data_source.authors(start_year=2018),
		[{'id':3, 'last-name':'Lewis', 'first-name':'Sinclair',
		'birth-year':1885, 'death-year': None},
		{'id':24, 'last-name':'Carré', 'first-name':'John Le',
		'birth-year':1931, 'death-year': None},
		{'id':2, 'last-name':'Morrison', 'first-name':'Toni',
		'birth-year':1931, 'death-year': None},
		{'id':0, 'last-name':'Willis', 'first-name':'Connie',
		'birth-year':1945, 'death-year': None},
		{'id':11, 'last-name':'Rushdie', 'first-name':'Salman',
		'birth-year':1947, 'death-year': None},
		{'id':12, 'last-name':'Bujold', 'first-name':'Lois McMaster',
		'birth-year':1949, 'death-year': None},
		{'id':16, 'last-name':'Murakami', 'first-name':'Haruki',
		'birth-year':1949, 'death-year': None},
		{'id':5, 'last-name':'Gaiman', 'first-name':'Neil',
		'birth-year':1960, 'death-year': None},
		{'id':20, 'last-name':'Jemisen', 'first-name':'N.K.',
		'birth-year':1972, 'death-year': None},
		{'id':18, 'last-name':'Alderman', 'first-name':'Naomi',
		'birth-year':1974, 'death-year': None}])

	def test_authors_end_year(self):
		self.assertEqual(self.books_data_source.authors(end_year=1817),
		[{'id':4, 'last-name':'Austen', 'first-name':'Jane',
		'birth-year':1775, 'death-year': 1817},
		{'id':23, 'last-name':'Dickens', 'first-name':'Charles',
		'birth-year':1812, 'death-year': 1870},
		{'id':7, 'last-name':'Brontë', 'first-name':'Charlotte',
		'birth-year':1816, 'death-year': 1855}])

	def test_authors_sort_by_other_value(self):
		self.assertEqual(self.books_data_source.authors(end_year=1817, sort_by="other_value"),
		[{'id':4,'last-name':'Austen','first-name':'Jane',
		'birth-year':1775, 'death-year': 1817},
		{'id':7, 'last-name':'Brontë', 'first-name':'Charlotte',
		'birth-year':1816, 'death-year': 1855},
		{'id':23, 'last-name':'Dickens', 'first-name':'Charles',
		'birth-year':1812, 'death-year': 1870}])

	def test_authors_start_end_year(self):
		self.assertEqual(self.books_data_source.authors(start_year=2018, end_year=2018),
		[{'id':3, 'last-name':'Lewis', 'first-name':'Sinclair',
		'birth-year':1885, 'death-year': None},
		{'id':24, 'last-name':'Carré', 'first-name':'John Le',
		'birth-year':1931, 'death-year': None},
		{'id':2, 'last-name':'Morrison', 'first-name':'Toni',
		'birth-year':1931, 'death-year': None},
		{'id':0, 'last-name':'Willis', 'first-name':'Connie',
		'birth-year':1945, 'death-year': None},
		{'id':11, 'last-name':'Rushdie', 'first-name':'Salman',
		'birth-year':1947, 'death-year': None},
		{'id':12, 'last-name':'Bujold', 'first-name':'Lois McMaster',
		'birth-year':1949, 'death-year': None},
		{'id':16, 'last-name':'Murakami', 'first-name':'Haruki',
		'birth-year':1949, 'death-year': None},
		{'id':5, 'last-name':'Gaiman', 'first-name':'Neil',
		'birth-year':1960, 'death-year': None},
		{'id':20, 'last-name':'Jemisen', 'first-name':'N.K.',
		'birth-year':1972, 'death-year': None},
		{'id':18, 'last-name':'Alderman', 'first-name':'Naomi',
		'birth-year':1974, 'death-year': None}])

	def test_authors_search_text_start_year(self):
		self.assertEqual(self.books_data_source.authors(search_text="wi", start_year=2018),
		[{'id':3, 'last-name':'Lewis', 'first-name':'Sinclair',
		'birth-year':1885, 'death-year': None},
		{'id':0, 'last-name':'Willis', 'first-name':'Connie',
		'birth-year':1945, 'death-year': None}])

	def test_authors_search_text_end_year(self):
		self.assertEqual(self.books_data_source.authors(search_text="en", end_year=1817),
		[{'id':4, 'last-name':'Austen', 'first-name':'Jane',
		'birth-year':1775, 'death-year': 1817},
		{'id':23, 'last-name':'Dickens', 'first-name':'Charles',
		'birth-year':1812, 'death-year': 1870}])

	def test_authors_search_text_sort_by_other(self):
		self.assertEqual(self.books_data_source.authors(search_text="en", sort_by="other value"),
		[{'id':4, 'last-name':'Austen', 'first-name':'Jane',
		'birth-year':1775, 'death-year': 1817},
		{'id':23, 'last-name':'Dickens', 'first-name':'Charles',
		'birth-year':1812, 'death-year': 1870},
		{'id':20, 'last-name':'Jemisen', 'first-name':'N.K.',
		'birth-year':1972, 'death-year': None},
		{'id':8, 'last-name':'Wodehouse', 'first-name':'Pelham Grenville',
		'birth-year':1881, 'death-year': 1975}])

if __name__ == '__main__':
	unittest.main()

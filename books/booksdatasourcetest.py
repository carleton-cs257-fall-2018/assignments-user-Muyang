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
	def test_book_no_id(self):
		self.assertRaises(ValueError, self.books_data_source.book, -1)

	#Testing the books method
	def test_books_author_id(self):
		self.assertEqual(self.books_data_source.books(author_id=22),
			[{'id':41, 'title':'Middlemarch','publication-year':1871}])
	def test_books_wrong_author_id(self):
		self.assertRaises(ValueError,self.books_data_source.books, author_id=-1)

	def test_books_search_text(self):
		self.assertEqual(self.books_data_source.books(search_text='middle'),
			[{'id':41, 'title':'Middlemarch','publication-year':1871}])

	def test_books_start_year(self):
		self.assertEqual(self.books_data_source.books(start_year=2016),
			[{'id':35, 'title':'The Power', 'publication-year':2016}])
	def test_books_wrong_start_year(self):
		self.assertRaises(ValueError, self.books_data_source.books, start_year=-1)

	def test_books_end_year(self):
		self.assertEqual(self.books_data_source.books(end_year=1813),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])
	def test_books_wrong_end_year(self):
		self.assertRaises(ValueError,self.books_data_source.books,end_year=-1)

	def test_books_author_id_with_start_year(self):
		self.assertEqual(self.books_data_source.books(author_id=4, start_year=1812),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813},
			{'id':5, 'title':'Emma', 'publication-year':1815}])
	def test_books_author_id_with_end_year(self):
		self.assertEqual(self.books_data_source.books(author_id=4, end_year=1817),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813},
			{'id':5, 'title':'Emma', 'publication-year':1815}])

	def test_books_search_text_with_start_year(self):
		self.assertEqual(self.books_data_source.books(search_text='THE', start_year=2016),
			[{'id':35, 'title':'The Power','publication-year':'2016'}])
	def test_books_search_text_with_end_year(self):
		self.assertEqual(self.books_data_source.books(search_text='AND', end_year=1830),
			[{'id':18, 'title':'Pride and Prejudice', 'publication-year':1813},
			{'id':20, 'title':'Sense and Sensibility', 'publication-year':1813}])

	def test_books_sort_by_default(self):
		self.assertEqual(self.books_data_source.books(),
			[{'id':30, 'title':'1Q84', 'publication-year':2009},
			{'id':31, 'titel':'A Wild Sheep Chase', 'publication-year':1982},
			{'id':0, 'title':'All Clear','publication-year':2010}])
	def test_books_sort_by_title(self):
		self.assertEqual(self.books_data_source.books(sort_by='title'),
			[{'id':30, 'title':'1Q84', 'publication-year':2009},
			{'id':31, 'titel':'A Wild Sheep Chase', 'publication-year':1982},
			{'id':0, 'title':'All Clear','publication-year':2010}])
	def test_books_sort_by_year(self):
		self.assertEqual(self.books_data_source.books(sort_by='year'),
			[{'id':31, 'titel':'A Wild Sheep Chase', 'publication-year':1982},
			{'id':30, 'title':'1Q84', 'publication-year':2009},
			{'id':0, 'title':'All Clear','publication-year':2010}])
	def test_books_wrong_sort_by(self):
		self.assertRaises(ValueError, self.books_data_source.books, sort_by='happiness')
	#Testing the books_for_author method
	def test_books_for_author(self):
		self.assertEqual(self.books_data_source.books_for_author(22),
			[{'id':41, 'title':'Middlemarch', 'publication-year':1871}])
	def test_books_for_author_wrong_id(self):
		self.assertRaises(self.books_data_source.books_for_author, -1)

	def test_author(self):
		self.assertEqual(self.books_data_source.author(22),
		{'id':22,'last_name':'Eliot','first_name':'George',
		'birth_year':1949,'death_year':None})

	def test_authors_book_id(self):
		self.assertEqual(self.books_data_source.authors(book_id=41),
		{"id":22, "last_name":"Eliot","first_name":"George",
		"birth_year":1949,"death_year":None})

	def test_authors_search_text(self):
		self.assertEqual(self.books_data_source.authors(search_text="je"),
		[{'id':21, 'last_name':'Jerome', 'first_name':'Jerome K.',
		'birth_year':1859, 'death_year': 1927},
		{'id':20, 'last_name':'Jemisen', 'first_name':'N.K',
		'birth_year':1972, 'death_year': None}])

	def test_authors_start_year(self):
		self.assertEqual(self.books_data_source.authors(start_year=1885),
		[{'id':3, 'last_name':'Lewis', 'first_name':'Sinclair',
		'birth_year':1885, 'death_year': None},
		{'id':2, 'last_name':'Morrison', 'first_name':'Toni',
		'birth_year':1931, 'death_year': None},
		{'id':24, 'last_name':'CarrÃ©', 'first_name':'John Le',
		'birth_year':1931, 'death_year': None},
		{'id':0, 'last_name':'Willis', 'first_name':'Connie',
		'birth_year':1945, 'death_year': None},
		{'id':11, 'last_name':'Rushdie', 'first_name':'Salman',
		'birth_year':1947, 'death_year': None},
		{'id':12, 'last_name':'Bujold', 'first_name':'Lois McMaster',
		'birth_year':1949, 'death_year': None},
		{'id':16, 'last_name':'Murakami', 'first_name':'Haruki',
		'birth_year':1949, 'death_year': None},
		{'id':5, 'last_name':'Gaiman', 'first_name':'Neil',
		'birth_year':1960, 'death_year': None},
		{'id':20, 'last_name':'Jemisen', 'first_name':'N.K.',
		'birth_year':1972, 'death_year': None},
		{'id':18, 'last_name':'Alderman', 'first_name':'Naomi',
		'birth_year':1974, 'death_year': None}])

	def test_authors_end_year(self):
		self.assertEqual(self.books_data_source.authors(end_year=1817),
		[{'id':4, 'last_name':'Austen', 'first_name':'Jane',
		'birth_year':1775, 'death_year': 1817},
		{'id':23, 'last_name':'Dickens', 'first_name':'Charles',
		'birth_year':1812, 'death_year': 1870},
		{'id':7, 'last_name':'BrontÃ«', 'first_name':'Charlotte',
		'birth_year':1816, 'death_year': 1855}])

	def test_authors_sort_by_other_value(self):
		self.assertEqual(self.books_data_source.authors(start_year=1817, sort_by="last_name"),
		[{'id':4,'last_name':'Austen','first_name':'Jane',
		'birth_year':1775, 'death_year': 1817},
		{'id':7, 'last_name':'BrontÃ«', 'first_name':'Charlotte',
		'birth_year':1816, 'death_year': 1855},
		{'id':23, 'last_name':'Dickens', 'first_name':'Charles',
		'birth_year':1812, 'death_year': 1870}])

	def test_authors_start_end_year(self):
		self.assertEqual(self.books_data_source.authors(start_year=1885, end_year=1974),
		[{'id':3, 'last_name':'Lewis', 'first_name':'Sinclair',
		'birth_year':1885, 'death_year': None},
		{'id':2, 'last_name':'Morrison', 'first_name':'Toni',
		'birth_year':1931, 'death_year': None},
		{'id':24, 'last_name':'CarrÃ©', 'first_name':'John Le',
		'birth_year':1931, 'death_year': None},
		{'id':0, 'last_name':'Willis', 'first_name':'Connie',
		'birth_year':1945, 'death_year': None},
		{'id':11, 'last_name':'Rushdie', 'first_name':'Salman',
		'birth_year':1947, 'death_year': None},
		{'id':12, 'last_name':'Bujold', 'first_name':'Lois McMaster',
		'birth_year':1949, 'death_year': None},
		{'id':16, 'last_name':'Murakami', 'first_name':'Haruki',
		'birth_year':1949, 'death_year': None},
		{'id':5, 'last_name':'Gaiman', 'first_name':'Neil',
		'birth_year':1960, 'death_year': None},
		{'id':20, 'last_name':'Jemisen', 'first_name':'N.K.',
		'birth_year':1972, 'death_year': None},
		{'id':18, 'last_name':'Alderman', 'first_name':'Naomi',
		'birth_year':1974, 'death_year': None}])

	def test_authors_search_text_start_year(self):
		self.assertEqual(self.books_data_source.authors(search_text="wi", start_year=1885),
		[{'id':3, 'last_name':'Lewis', 'first_name':'Sinclair',
		'birth_year':1885, 'death_year': None},
		{'id':0, 'last_name':'Willis', 'first_name':'Connie',
		'birth_year':1945, 'death_year': None}])

	def test_authors_search_text_end_year(self):
		self.assertEqual(self.books_data_source.authors(search_text="ens", end_year=1870),
		[{'id':4, 'last_name':'Austen', 'first_name':'Jane',
		'birth_year':1775, 'death_year': 1817},
		{'id':23, 'last_name':'Dickens', 'first_name':'Charles',
		'birth_year':1812, 'death_year': 1870}])

	def test_authors_search_text_sort_by_other(self):
		self.assertEqual(self.books_data_source.authors(search_text="en", sort_by="last_name"),
		[{'id':4, 'last_name':'Austen', 'first_name':'Jane',
		'birth_year':1775, 'death_year': 1817},
		{'id':23, 'last_name':'Dickens', 'first_name':'Charles',
		'birth_year':1812, 'death_year': 1870},
		{'id':20, 'last_name':'Jemisen', 'first_name':'N.K.',
		'birth_year':1972, 'death_year': None},
		{'id':8, 'last_name':'Wodehouse', 'first_name':'Pelham Grenville',
		'birth_year':1881, 'death_year': 1975}])

if __name__ == '__main__':
	unittest.main()

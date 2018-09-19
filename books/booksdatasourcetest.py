'''
	booksdatasourcetest.py
	Muyang Shi, Justin T. Washington 18 Sept 2018
'''

import booksdatasource
import unittest

class booksdatasourcetest(unittest.TestCase):
	def setUp(self):
		self.books_data_source = booksdatasource.BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')

	def tearDown(self):
		pass

	def test_books(self):
		pass
	def test_authors(self):
		pass
	def test_books_authors_links(self):
		pass
if __name__ == '__main__':
	unittest.main()
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
	def test_book(self):
		self.assertEqual(self.books_data_source.book(41),{'id':41,'title':'Middlemarch','publication-year':1871})
	def test_books(self):
		self.assertEqual(self.books_data_source.books(author_id=22),[{'id':41, 'title':'Middlemarch','publication-year':1871}])
	def test_authors(self):
		self.assertEqual(self.books_data_source.author(22), {'id':22, 'last_name':'Eliot', 'first_name':'George', 'birth_year':1949, 'death_year': None})
	def test_books_authors_links(self):
		pass
if __name__ == '__main__':
	unittest.main()
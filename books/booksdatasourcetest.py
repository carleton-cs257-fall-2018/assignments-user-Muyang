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
		self.assertEqual(self.books_data_source.book(41),
			{'id':41,'title':'Middlemarch','publication-year':1871})
	def test_book_no_id(self):
		self.assertRaises(ValueError, self.books_data_source.book, -1)

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

	def test_author(self):
		self.assertEqual(self.books_data_source.author(22), 
			{'id':22, 'last_name':'Eliot', 'first_name':'George', 'birth_year':1949, 'death_year': None})
	def test_books_authors_links(self):
		pass
if __name__ == '__main__':
	unittest.main()
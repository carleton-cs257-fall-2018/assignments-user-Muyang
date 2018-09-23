import sys, csv

books_list = []

books_csv = csv.reader(open('books.csv'))
authors_csv = csv.reader(open('authors.csv'))
link_csv = csv.reader(open('books_authors.csv'))

for book in books_csv:
	if book[2] != None:
		publication = int(book[2])
	book_dictionary = {'id': int(book[0]), 'title':book[1], 'publication-year': publication}
	books_list.append(book_dictionary)
print(books_list)


for book in books_list:
	print(book)
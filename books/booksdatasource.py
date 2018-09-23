#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''
import sys, csv
class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''
    books_list = []
    authors_list = [{'id':22,'last_name':'Eliot','first_name':'George','birth_year':1949,'death_year':None}]
    books_authors_link_list = [{'book_id':41, 'author_id':22}]

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871
                    

                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6
                  
                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''
        books_csv = csv.reader(open(books_filename))
        authors_csv = csv.reader(open(authors_filename))
        link_csv = csv.reader(open(books_authors_link_filename))

        for book in books_csv:
            book_dictionary = {'id': int(book[0]), 'title':book[1], 'publication-year':book[2]}
            self.books_list.append(book_dictionary)

        pass

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.)
        
            Raises ValueError if book_id is not a valid book ID.
        '''
        if book_id != None and type(book_id) == int and book_id >= 0:
            for book in self.books_list:
                if int(book.get('id')) == book_id:
                    return book
        else:
            raise ValueError

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            See the BooksDataSource comment for a description of how a book is represented.

            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises TypeError if search_text or sort_by is non-None, but not a string.

            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
        '''
        result_list = []
        if author_id != None:
            result_list = self.books_with_author_id(author_id)

        if search_text != None:
            if len(result_list) == 0:
                result_list = self.books_with_search_text(search_text, self.books_list)
            else:
                result_list = self.books_with_search_text(search_text, result_list)

        if start_year != None:
            if len(result_list) == 0:
                result_list = self.books_with_start_year(start_year, self.books_list)
            else:
                result_list = self.books_with_start_year(start_year, result_list)
        if end_year != None:
            if len(result_list) == 0:
                result_list= self.books_with_end_year(end_year, self.books_list)
            else:
                result_list = self.books_with_end_year(end_year, self.result_list)
        return result_list

    def books_with_start_year(self, start_year, books_list):
        if type(start_year) != int:
            raise TypeError
        else:
            book_list = []
            for book in books_list:
                if start_year - book.get('publication-year') >= 0:
                    book_list.append(book)
            return book_list
    def books_with_end_year(self, end_year, books_list):
        if type(end_year) != int:
            raise TypeError
        else:
            book_list = []
            for book in books_list:
                if end_year - book.get('publication-year') <= 0:
                    book_list.append(book)
            return book_list

    def books_with_search_text(self, search_text, books_list):
        if type(search_text) == str:
            book_list = []
            for book in books_list:
                if search_text.lower() in book.get('title').lower():
                    book_list.append(book)
            return book_list
        else:
            raise TypeError

    def books_with_author_id(self, author_id):
        if type(author_id) == int and author_id >= 0: 
            book_id_list = []
            book_list = []
            for book_author_dict in self.books_authors_link_list:
                if book_author_dict.get('author_id') == author_id:
                    book_id_list.append(book_author_dict.get('book_id'))
            for book_id in book_id_list:
                book_list.append(self.book(book_id))
            return book_list
        else:
            raise ValueError

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)
        
            Raises ValueError if author_id is not a valid author ID.
        '''
        return {}

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year
        
            See the BooksDataSource comment for a description of how an author is represented.
        '''
        return []


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.authors(book_id=book_id)

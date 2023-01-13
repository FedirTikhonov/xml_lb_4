from rdflib import Graph, URIRef


class Author:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.books_translated = []
        self.books_written = []
        self.lives_in = None

    def __str__(self):
        return f'Name={self.name}\nID={self.id}\n'


class Book:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.translator = None

    def __str__(self):
        return str(f"\n-----\nBook ID={self.id}\nBook Name={self.name}\n--------")


class Translator:
    def __init__(self):
        self.id = ''
        self.lives_in = None
        self.name = ''
        self.books_translated = []


def task_4_function():
    author_tree = Graph()
    author_tree.parse("authors.rdf", format='xml')
    class_uri = URIRef('http://example.org/lit#authorName')
    author_arr = []
    for s, p, o in author_tree.triples((None, class_uri, None)):
        curr_author = Author()
        curr_author.id = str(s)
        curr_author.name = str(o)
        author_arr.append(curr_author)
    class_uri = URIRef('http://example.org/lit#hasWritten')
    for s, p, o in author_tree.triples((None, class_uri, None)):
        for author in author_arr:
            if str(s) == author.id:
                author.books_written.append(str(o))
    book_tree = Graph()
    book_arr = []
    book_tree.parse("books.rdf", format='xml')
    for s, p, o in book_tree.triples((None, None, None)):
        new_book = Book()
        new_book.id = str(s)
        new_book.name = str(o)
        book_arr.append(new_book)

    translator_tree = Graph()
    translator_arr = []
    translator_tree.parse("translators.rdf", format='xml')
    class_uri = URIRef("http://example.org/lit#authorName")
    for s, p, o in translator_tree.triples((None, class_uri, None)):
        new_translator = Translator()
        new_translator.name = str(o)
        new_translator.id = str(s)
        translator_arr.append(new_translator)
    class_uri = URIRef("http://example.org/lit#hasTranslated")
    for s, p, o in translator_tree.triples((None, class_uri, None)):
        for translator in translator_arr:
            if str(s) == translator.id:
                translator.books_translated.append(str(o))

    for book in book_arr:
        for author_index in range(len(author_arr)):
            for book_index in range(len(author_arr[author_index].books_written)):
                if book.id == author_arr[author_index].books_written[book_index]:
                    author_arr[author_index].books_written[book_index] = book

    for book in book_arr:
        i = 2
        for translator_index in range(len(translator_arr)):
            for book_index in range(len(translator_arr[translator_index].books_translated)):
                book_id = book.id
                translated_book = translator_arr[translator_index].books_translated[book_index]
                if book_id == translated_book:
                    translator_arr[translator_index].books_translated[book_index] = book

    for translator_index in range(len(translator_arr)):
        for book_index in range(len(translator.books_translated)):
            translator_arr[translator_index].books_translated[book_index].translator = translator_arr[translator_index]

    living_tree = Graph()
    living_tree.parse("locations.rdf", format='xml')
    for s, p, o in living_tree.triples((None, None, None)):
        for author in author_arr:
            if author.id == str(s):
                author.lives_in = str(o)
        for translator in translator_arr:
            if translator.id == str(s):
                translator.lives_in = str(o)
    for author in author_arr:
        if len(author.books_written) != 0:
            if author.lives_in is not None:
                print(f"{author.name} ({author.lives_in}) wrote:")
            else:
                print(f"{author.name} wrote:")
            for book in author.books_written:
                print(f"\t{book.name}")
                if book.translator is not None:
                    if book.translator.lives_in is not None:
                        print(f"\t\tTranslated by {book.translator.name} ({book.translator.lives_in})")
                    else:
                        print(f"\t\tTranslated by {book.translator.name}")








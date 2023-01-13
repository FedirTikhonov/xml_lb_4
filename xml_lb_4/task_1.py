from rdflib import Graph, URIRef


class Author:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.books_translated = []
        self.books_written = []
        self.lives_in = ''

    def __str__(self):
        return f'Name={self.name}\nID={self.id}\n'


class Book:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.author = ''


def task_1_function():
    tree = Graph()
    tree.parse("authors.rdf", format='xml')
    class_uri = URIRef('http://example.org/lit#authorName')
    author_arr = []
    for s, p, o in tree.triples((None, class_uri, None)):
        curr_author = Author()
        curr_author.id = str(s)
        curr_author.name = str(o)
        author_arr.append(curr_author)
    class_uri = URIRef('http://example.org/lit#hasWritten')
    for s, p, o in tree.triples((None, class_uri, None)):
        for author in author_arr:
            if str(s) == author.id:
                author.books_written.append(str(o))

    print("<rdf:RDF xmlns:lit=\"http://example.org/lit#\"\nxmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">")
    for author in author_arr:
        print(f"\t<rdf:Description rdf:about=\"{author.id}\">")
        print(f"\t\t<lit:authorName>{author.name}</lit:authorName>")
        for book in author.books_written:
            print(f"\t\t<lit:hasWritten rdf:resource=\"{book}\"/>")
        print(f"\t</rdf:Description>")
    print("</rdf:RDF>")




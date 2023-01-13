import rdflib


def task_25_function():
    tree = rdflib.Graph()
    tree.parse("Schulpersonal.rdf", format="xml")
    tree.parse("Schulpers.owl", format="xml")

    per = rdflib.Namespace("http://example.org/personal/per#")

    query = """
        ASK {
        per:caretaker rdfs:subClassOf per:teacher
        }
    """
    results = tree.query(query)
    if results.askAnswer:
        print("Caretaker is a teacher")
    else:
        print("Caretaker is not a teacher")

    query = """
            ASK {
        per:caretaker rdfs:subClassOf per:student
        }
        """
    results = tree.query(query)
    if results.askAnswer:
        print("Caretaker is a student")
    else:
        print("Caretaker is not a student")

    query = """
        ASK {
        per:caretaker rdfs:subClassOf per:employee
        }
            """
    results = tree.query(query)
    if results.askAnswer:
        print("Caretaker is an employee")
    else:
        print("Caretaker is not an employee")

    second_tree = rdflib.Graph()
    second_tree.parse("Schulpersonal.rdf", format="xml")
    second_tree.parse("Schulpers.owl", format="xml")
    query = """
           ASK {
           per:caretaker rdfs:subClassOf per:employee
           } 
               """
    results = tree.query(query)
    second_query = """
               ASK {
               per:employee rdfs:subClassOf per:person
               } 
                   """
    second_results = second_tree.query(query)
    if results.askAnswer and second_results.askAnswer:
        print("Caretaker is a person")
    else:
        print("Caretaker is not a person")


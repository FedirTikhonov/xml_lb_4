import rdflib


def task_22_function():
    tree = rdflib.Graph()
    tree.parse("Schulpersonal.rdf", format="xml")
    tree.parse("Schulpers.owl", format="xml")

    per = rdflib.Namespace("http://example.org/personal/per#")

    query = """
        SELECT ?brother
        WHERE {
            ?brother per:isBrother ?x .
            FILTER NOT EXISTS {
                ?brother rdf:type per:teacher .
            }
        }
    """

    results = tree.query(query)
    for brother in results:
        print("Brother: ", brother)

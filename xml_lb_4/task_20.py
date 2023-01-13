import rdflib
import owlrl


def task_20_function():
    tree = rdflib.Graph()
    tree.parse("Schulpersonal.rdf", format="xml")
    tree.parse("Schulpers.owl")

    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(tree)

    uri = rdflib.URIRef("http://example.org/personal/per#isChild")
    for s, p, o in tree.triples((None, uri, None)):
        print(f"{s} is the father of {o}")
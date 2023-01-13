import rdflib
import owlrl


def task_21_function():
    tree = rdflib.Graph()
    tree.parse("Schulpersonal.rdf", format="xml")
    tree.parse("Schulpers.owl")

    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(tree)

    uri = rdflib.URIRef("http://example.org/personal/per#isRelative")
    for s, p, o in tree.triples((None, uri, None)):
        print(f"{s} is a relative of {o}")
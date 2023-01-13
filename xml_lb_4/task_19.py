import rdflib
import owlrl


def task_19_function():
    tree = rdflib.Graph()
    tree.parse("Schulpersonal.rdf", format="xml")
    tree.parse("Schulpers.owl")

    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(tree)

    uri = rdflib.URIRef("http://example.org/personal/per#isBrother")
    for s, p, o in tree.triples((None, uri, None)):
        print(f"{s} is the brother of {o}")
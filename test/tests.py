#!/usr/bin/env python3
import pytest
import rdflib


def test_loading_graph():
    data = """@prefix : <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        <> :value _:a .
        _:a :first "turtles"; :rest _:a .
        """

    g = rdflib.Graph()
    g.parse(data=data, format="turtle")

    assert len(g) == 3
    assert rdflib.term.Literal("turtles") in g.objects()

    predicates = []

    for pred in g.predicates():
        predicates.append(pred)

    predicates.sort()
    correct_predicates = [rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#first'),
                          rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#rest'),
                          rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#value')]

    assert predicates == correct_predicates

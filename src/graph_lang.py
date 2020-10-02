#!/usr/bin/env python3
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from cyk import parse_graph

def build_automata_from_graph(filename):
    automata = NondeterministicFiniteAutomaton()
    graph = parse_graph(filename)
    vert = set()
    for u, symb, v in graph:
        vert.add(u)
        vert.add(v)
    for v in vert:
        automata.add_start_state(State((filename, v)))
        automata.add_final_state(State((filename, v)))
    for u, symb, v in graph:
        automata.add_transition(State((filename, u)), Symbol(symb), State((filename, v)))


def intersec(automata1, automata2):
    return automata1.get_intersection(automata2)


def union(automata1, automata2):
    return compl(intersec(compl(automata1), compl(automata2)))


def compl(automata):
    return automata.get_complement()


def graph_lang_intersect(prods, automata, graph):
    pass

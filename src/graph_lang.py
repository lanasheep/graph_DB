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

    return automata.minimize()


def universal():
    automata = NondeterministicFiniteAutomaton()
    node = State(("", 0))
    automata.add_start_state(node)
    automata.add_final_state(node)
    for chr in "abcdefghijklmnopqrstuvwxyz":
        automata.add_transition(node, Symbol(chr), node)

    return automata


def intersec(automata1, automata2):
    return automata1.get_intersection(automata2).minimize()


def union(automata1, automata2):
    return compl(intersec(compl(automata1), compl(automata2))).minimize()


def compl(automata):
    return universal().get_difference(automata).minimize()


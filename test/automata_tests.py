#!/usr/bin/env python3
import pytest
from automata import reg2min_dfa
from automata import dfa_nfa_intersection
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton


def test_reg2min_dfa1():
    dfa = reg2min_dfa("a")
    a = Symbol("a")

    assert len(dfa.states) == 2
    assert dfa.get_number_transitions() == 1
    assert dfa.is_deterministic() 
    assert dfa.accepts([a]) == True
    

def test_reg2min_dfa2():
	dfa = reg2min_dfa("a(b|c)*d")
	a = Symbol("a")
	b = Symbol("b")
	c = Symbol("c")
	d = Symbol("d")

	assert len(dfa.states) == 3
	assert dfa.get_number_transitions() == 4
	assert dfa.is_deterministic() 
	assert dfa.accepts([a, d]) == True
	assert dfa.accepts([a, b, d]) == True
	assert dfa.accepts([a, c, d]) == True
	assert dfa.accepts([b, d]) == False


def test_reg2min_dfa3():
	dfa = reg2min_dfa("(a|b)*(b|c)*")
	a = Symbol("a")
	b = Symbol("b")
	c = Symbol("c")

	assert len(dfa.states) == 2
	assert dfa.get_number_transitions() == 5
	assert dfa.is_deterministic() 
	assert dfa.accepts([a, b]) == True
	assert dfa.accepts([b, a]) == True
	assert dfa.accepts([a, c, c]) == True
	assert dfa.accepts([a, c, a]) == False


def test_dfa_nfa_intersection1():
	dfa = DeterministicFiniteAutomaton()
	nfa = NondeterministicFiniteAutomaton()
	a = Symbol("a")
	b = Symbol("b")
	dst0 = State("dst0")
	dst1 = State("dst1")
	nst0 = State("nst0")
	nst1 = State("nst1")
	dfa.add_start_state(dst0)
	dfa.add_final_state(dst1)
	nfa.add_start_state(nst0)
	nfa.add_final_state(nst1)
	dfa.add_transition(dst0, a, dst1)
	dfa.add_transition(dst0, b, dst1)
	nfa.add_transition(nst0, a, nst0)
	nfa.add_transition(nst0, a, nst1)
	nfa.add_transition(nst0, b, nst1)
	intersec = dfa_nfa_intersection(dfa, nfa)

	assert intersec.accepts([a]) == True
	assert intersec.accepts([b]) == True
	assert intersec.accepts([a, b]) == False


def test_dfa_nfa_intersection2():
	dfa = DeterministicFiniteAutomaton()
	nfa = NondeterministicFiniteAutomaton()
	a = Symbol("a")
	b = Symbol("b")
	c = Symbol("c")
	dst0 = State("dst0")
	dst1 = State("dst1")
	dst2 = State("dst2")
	nst0 = State("nst0")
	nst1 = State("nst1")
	nst2 = State("nst2")
	dfa.add_start_state(dst0)
	dfa.add_final_state(dst1)
	dfa.add_final_state(dst2)
	nfa.add_start_state(nst0)
	nfa.add_final_state(nst2)
	dfa.add_transition(dst0, a, dst1)
	dfa.add_transition(dst1, b, dst2)
	nfa.add_transition(nst0, a, nst1)
	nfa.add_transition(nst1, b, nst0)
	nfa.add_transition(nst1, b, nst2)
	nfa.add_transition(nst1, c, nst2)
	intersec = dfa_nfa_intersection(dfa, nfa)

	assert intersec.accepts([a]) == False
	assert intersec.accepts([b]) == False
	assert intersec.accepts([a, b]) == True

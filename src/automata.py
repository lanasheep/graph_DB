#!/usr/bin/env python3
from pyformlang.regular_expression import Regex


def reg2min_dfa(str):
    reg = Regex(str)
    return reg.to_epsilon_nfa().minimize()


def dfa_nfa_intersection(dfa, nfa):
    assert dfa.is_deterministic()
    return dfa.get_intersection(nfa)

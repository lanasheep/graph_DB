#!/usr/bin/env python3
import os
from chomsky import to_CNF
from chomsky import parse_grammar
from cyk import CYK


def check(text):
    start, prods = to_CNF(parse_grammar(os.path.normpath("src/resources/grammar.txt")), "SCRIPT")
    if text and not text.isupper():
        return False
    text = text.lower().replace("\n", " ").split(" ")

    return CYK(start, prods, text)

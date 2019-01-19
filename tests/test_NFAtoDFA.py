from default.state_machines import NFA_to_DFA_convertor as convertor
from tests.some_nfa import *

def test_dfa_exercise3_6_4():
    nfa = nfa_exercise3_6_4()
    dfa = convertor(nfa)
    print(dfa)

def test_dfa_figure3_26():
    nfa = nfa_figure3_26()
    dfa = convertor(nfa)
    print(dfa)

def test_dfa_real_number_regex_demo():
    nfa = nfa_real_number_regex_demo()
    dfa = convertor(nfa)
    print(dfa)

def test_dfa_real_number_regex():
    nfa = nfa_real_number_regex()
    dfa = convertor(nfa)
    print(dfa)

test_dfa_real_number_regex()
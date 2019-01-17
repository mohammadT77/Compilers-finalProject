from default.state_machines import DFA,NFA,EP,State


def NFA_to_DFA_convertor(nfa,alfbt=None):
    convert_table = {}
    dfa_builder = DFA.Builder()


    def __set_alfabet():
        alfabet = nfa.get_alfabet() if alfbt is None else alfbt
        if alfabet is None: alfabet = nfa.find_alfabet()
        if alfabet is not None:
            if EP in alfabet: alfabet.remove(EP)

        return alfabet

    alfabet = __set_alfabet()
    if alfabet is None: raise Exception("alfabet error")
    dfa_builder.set_alfabet(alfabet)

    def hash_states(states):
        res = ""
        for x in states:
            res+=x.get_state_name()+"|"
        return res[0:-1]

    def __add_state(states):
        print("states",hash_states(states))
        print("\t",convert_table)
        if hash_states(states) not in convert_table:
            convert_table[hash_states(states)] = None
            map = {}
            for sym in alfabet:
                temp_ary = nfa.ep_closure(nfa.move(states,sym))
                map[sym] = temp_ary
                __add_state(temp_ary)
            convert_table[hash_states(states)] = map
            # print("\t'", convert_table)
        else: return;

    start_state_ary = nfa.ep_closure(nfa.get_start_state())
    __add_state(start_state_ary)
    # for s in convert_table:
    #     print(s,[str(c.get_state_name()) for c in s])
    # print(start_state_ary) #TODO trace
    # temp_ary=start_state_ary
    # count = 1
    # for state in
    #     for symb in alfabet:
    #         temp_ary = nfa.ep_closure(nfa.move(temp_ary,symb))
    #         if temp_ary not in convert_table:
    #             convert_table.append(temp_ary)
    #         else:

def test():
    state_S = State('S', {
        EP: 'E'
    })
    state_A = State('A', {
        EP:'B'
    })
    state_B = State('B', {'b': 'B'})
    state_E = State('E',{'a':'A','b': 'B'})

    nfab = NFA.Builder()
    nfab.add_state(state_A, True)
    nfab.add_state(state_B)
    nfab.set_startstate(state_S)
    nfab.add_state(state_E)
    nfa = nfab.build()
    dfa = NFA_to_DFA_convertor(nfa)


def test_exercise3_6_4():
    # Exercise 3.6.4 of Compiler book
    state = [
        State('0',{'a':'1',EP:'3'}),
        State('1',{'b':'2',EP:'0'}),
        State('2',{'b':'3',EP:'1'}),
        State('3',{'a':'0',EP:'2'}),
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_startstate(state[0])
    nfa_builder.add_state(state[1])
    nfa_builder.add_state(state[2])
    nfa_builder.add_state(state[3],True)
    nfa = nfa_builder.build()
    # print([x.get_state_name() for x in nfa.ep_closure(state[3])])
    dfa = NFA_to_DFA_convertor(nfa)


# test()
test_exercise3_6_4()
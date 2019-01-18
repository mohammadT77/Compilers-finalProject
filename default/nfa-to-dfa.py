from default.state_machines import DFA,NFA,EP,State
from default.state import hash_state_list as hash_states


def NFA_to_DFA_convertor(nfa,alfbt=None):
    convert_table = {}
    newgoal_states = []
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

    def __add_state(states):
        # print("\n------------\n\tstates",hash_states(states)) #TODO trace
        if hash_states(states) not in convert_table:
            convert_table[hash_states(states)] = None
            for s in states:
                if nfa.is_goal(s):newgoal_states.append(hash_states(states))
            # print("\tconvrt_tbl",convert_table) #TODO trace
            map = {}
            for sym in alfabet:
                move_ary = nfa.move(states,sym)
                temp_ary = nfa.ep_closure(move_ary)
                # print('\t\tsym',sym,":") #TODO trace
                # print('\t\t\tmove:',hash_states(move_ary)) #TODO trace
                # print('\t\t\ttemp:',hash_states(temp_ary)) #TODO trace
                __add_state(temp_ary)
                map[sym] = hash_states(temp_ary)
            convert_table[hash_states(states)] = map
            # return map
            # print("\tnew cnvrttbl", convert_table) #TODO trace
        else: return;

    start_state_ary = nfa.ep_closure(nfa.get_start_state())
    print("sss",hash_states(start_state_ary)) #TODO trace
    __add_state(start_state_ary)
    # print("\nCONVERT_TABLE:",convert_table)
    # print("\nNEWGOAL_STATES:",newgoal_states)

    for cs in convert_table:
        state = State(cs,convert_table[cs])
        if cs==hash_states(start_state_ary):
            dfa_builder.set_startstate(state)
        else:
            dfa_builder.add_state(state,True if state.get_state_name() in newgoal_states else False)

    return dfa_builder.build()

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




# def test():
#     state_S = State('S', {
#         EP: 'E'
#     })
#     state_A = State('A', {
#         EP:'B'
#     })
#     state_B = State('B', {'b': 'B'})
#     state_E = State('E',{'a':'A','b': 'B'})
#
#     nfab = NFA.Builder()
#     nfab.add_state(state_A, True)
#     nfab.add_state(state_B)
#     nfab.set_startstate(state_S)
#     nfab.add_state(state_E)
#     nfa = nfab.build()
#     # dfa = NFA_to_DFA_convertor(nfa)


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
    # print(hash_states((nfa.move(state[3],'a'))))
    # print(hash_states([state[0]]+state[-1:0:-1]))
    # print("sds",hash_states(nfa.ep_closure(nfa.get_start_state())))
    dfa = NFA_to_DFA_convertor(nfa)
    # print(nfa.ep_closure(state[0]))
    print(dfa)

    del nfa_builder,state


def test_figure3_26():
    # Exercise 3.6.4 of Compiler book
    state = [
        State('0',{EP:['1','3']}),
        State('1',{'a':'2'}),
        State('2',{'a':'2'}),
        State('3',{'b':'4'}),
        State('4',{'b':'4'}),
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_startstate(state[0])
    nfa_builder.add_state(state[1])
    nfa_builder.add_state(state[2],True)
    nfa_builder.add_state(state[3])
    nfa_builder.add_state(state[4],True)
    nfa = nfa_builder.build()
    # print([x.get_state_name() for x in nfa.ep_closure(state[0])])
    # print([x.get_state_name() for x in nfa.ep_closure(nfa.move([state[0:4:-1]],'a'))])
    dfa = NFA_to_DFA_convertor(nfa)
    print(dfa)

# test()
# test_exercise3_6_4()
test_figure3_26()
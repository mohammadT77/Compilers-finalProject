from default.state_machines import *
EP = 'epsilon'
state_S = State('S',{
    'b': ['B','E'],
    EP : ['E','B']
})
state_A = State('A',{
    'b': 'B'
})
state_B = State('B',{EP:'C'})
state_E = State('E')
state_C = State('C',{EP:'A'})

def test_statemachine_builder():
    smb = StateMachine.Builder()
    smb.add_state(state_A,True)
    smb.add_state(state_B)
    smb.set_startstate(state_S)
    smb.add_state(state_E)
    sm = smb.build()

    print(sm.get_state_by_name(''))

def test_nfa1():
    nfab = NFA.Builder()
    nfab.add_state(state_A, True)
    nfab.add_state(state_B)
    nfab.set_startstate(state_S)
    nfab.add_state(state_E)
    nfab.add_state(state_C)
    nfa = nfab.build()
    print([s.get_state_name() for s in nfa.ep_closure(nfa.move([state_S,state_B],'b'))])

def test_nfa2():
    nfab = NFA.Builder()
    nfab.add_state(state_A, True)
    nfab.add_state(state_B)
    nfab.set_startstate(state_S)
    nfab.add_state(state_E)
    nfab.add_state(state_C)
    nfa = nfab.build()
    print([s.get_state_name() for s in nfa.ep_closure([state_S])])

def test_dfa():
    state0 =State('s0',{'a':'s1','b':'s0'})
    state1 = State('s1',{'a':'s1','b':'s2'})
    state2 = State('s2',{'a':'s1','b':'s2'})
    dfab = DFA.Builder()
    dfab.set_alfabet(['a','b'])
    dfab.set_startstate(state0)
    dfab.add_state(state1)
    dfab.add_state(state2,True)
    dfa = dfab.build()
    print(dfa)

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
    # dfa = NFA_to_DFA_convertor(nfa)




# test_statemachine_builder()
# test_nfa1()
# test_nfa2()
# test_dfa()
# test_figure3_26()
test_exercise3_6_4()




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

# test_statemachine_builder()
# test_nfa1()
test_nfa2()
# test_dfa()


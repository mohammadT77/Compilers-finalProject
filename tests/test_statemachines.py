from default.state_machines import *
EP = 'epsilon'
state_S = State('S',{
    'a': ['A','E'],
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
    nfa = nfab.build()
    print(NFA.move([state_S,state_B],'a'))

def test_nfa2():
    nfab = NFA.Builder()
    nfab.add_state(state_A, True)
    nfab.add_state(state_B)
    nfab.set_startstate(state_S)
    nfab.add_state(state_E)
    nfab.add_state(state_C)
    nfa = nfab.build()
    print([s.get_state_name() for s in nfa.ep_closure([state_S])])

# test_statemachine_builder()
# test_nfa1()
test_nfa2()



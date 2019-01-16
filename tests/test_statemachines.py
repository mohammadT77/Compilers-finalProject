from default.state_machines import *

state_S = State('S',{
    'a': 'A',
    EP : 'E',
    'b': 'B'
})
state_A = State('A',{
    'b': 'B'
})
state_B = State('B',{})
state_E = State('E')

def test_statemachine_builder():
    smb = StateMachine.Builder()
    smb.add_state(state_A,True)
    smb.add_state(state_B)
    smb.set_startstate(state_S)
    smb.add_state(state_E)
    sm = smb.build()
    print([d.get_state_name() for d in sm.get_goalstates()])



test_statemachine_builder()



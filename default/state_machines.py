from default.state import State

class StateMachine:

    _startstate = None
    _alfabet = None
    _states = None
    _goalstates = None



    @staticmethod
    def check_by_alfabet(state,alfabet):
        if alfabet is None: return True
        else:
            for s in state.get_childs():
                if s not in alfabet: return False
            return True

    class Builder:
        __startstate = None
        __alfabet = None
        __states = None
        __goalstates = None

        def add_state(self,state,is_goal=False):

            if not StateMachine.check_by_alfabet(state,self.__alfabet):
                raise ValueError("Alfabet not allowed")
            if self.__states is None: self.__states = [state]
            elif state in self.__states: return ;
            else:
                self.__states.append(state)
            if is_goal:
                if self.__goalstates is None:
                    self.__goalstates = [state]
                else:
                    self.__goalstates.append(state)


        def set_startstate(self,startstate):
            if not StateMachine.check_by_alfabet(startstate,self.__alfabet):
                raise ValueError("Alfabet not allowed")
            self.__startstate = startstate
            self.add_state(startstate,False)

        def set_alfabet(self,alfabet):
            self.__alfabet = alfabet

        def __check_all(self):
            res = []
            if self.__startstate is None: res.append('start_state')
            if self.__goalstates is None: res.append('goal_state')
            for s in self.__states:
                if not StateMachine.check_by_alfabet(s,self.__alfabet):
                    res.append('alfabet')

            return True if len(res)==0 else res


        def build(self):
            if type(self.__check_all()) == list:
                raise Exception(self.__check_all())
            return StateMachine(self.__startstate.get_state_name(),
                                self.__states,
                                [g.get_state_name() for g in self.__goalstates],
                                self.__alfabet)



    def __init__(self, start_state_name, states, goal_states_name, alfabet=None):
        if alfabet is not None and type(alfabet) == list:
            self._alfabet = alfabet
        if type(states) != list: raise TypeError( "states must be LIST")
        for s in states:
            if type(s) != State: raise TypeError( "state entities must be STATE")
            if self._alfabet is not None:
                for symbol in s.get_childs():
                    if symbol not in alfabet: raise ValueError( "Alfabet not matched")

        if type(goal_states_name) != list or len(goal_states_name)==0: raise TypeError("goal states must be LIST")

        self._states = states
        self._startstate = self.get_state_by_name(start_state_name)

        self._goalstates = []
        for g in goal_states_name:
            self._goalstates.append(self.get_state_by_name(g))

    def get_state_by_name(self,name):
        for state in self._states:
            if state.get_state_name() == name: return state
        return None

    def get_states(self):
        return self._states

    def get_goalstates(self):
        return self._goalstates

    def __str__(self):
        string_res = ""

        for s in self._states:
            string_res += str(s)

        return string_res




    def get_start_state(self):
        return self._startstate

    def is_goal(self,state_name):
        return state_name in [g.get_state_name() for g in self._goalstates]




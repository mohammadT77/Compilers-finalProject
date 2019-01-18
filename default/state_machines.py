from default.state import State,hash_state_list
from copy import copy,deepcopy


class StateMachine:

    _startstate = None
    _alfabet = None
    _states = None
    _goalstates = None

    @staticmethod
    def is_state_exist(state,states):
        for s in states:
            if state == s:
                return True
        return False


    @staticmethod
    def check_by_alfabet(state,alfabet):
        if alfabet is None: return True
        else:
            for s in state.get_childs():
                if s not in alfabet: return False
            return True

    class Builder:
        _startstate = None
        _alfabet = None
        _states = None
        _goalstates = None

        def add_state(self,state,is_goal=False):

            if not StateMachine.check_by_alfabet(state, self._alfabet):
                raise ValueError("Alfabet not allowed")
            if self._states is None: self._states = [state]
            elif state in self._states: return ;
            else:
                self._states.append(state)
            if is_goal:
                if self._goalstates is None:
                    self._goalstates = [state]
                else:
                    self._goalstates.append(state)


        def set_startstate(self,startstate):
            if not StateMachine.check_by_alfabet(startstate, self._alfabet):
                raise ValueError("Alfabet not allowed")
            self._startstate = startstate
            self.add_state(startstate,False)

        def set_alfabet(self,alfabet):
            self._alfabet = alfabet

        def check_all(self):
            res = []
            if self._startstate is None: res.append('start_state')
            if self._goalstates is None: res.append('goal_state')
            for s in self._states:
                if not StateMachine.check_by_alfabet(s, self._alfabet):
                    res.append('alfabet')

            return True if len(res)==0 else res


        def build(self):
            if type(self.check_all()) == list:
                raise Exception(self.check_all())
            return StateMachine(self._startstate.get_state_name(),
                                self._states,
                                [g.get_state_name() for g in self._goalstates],
                                self._alfabet)



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
            if state.get_state_name() == name: return copy(state)
        return None

    def get_alfabet(self):
        return deepcopy(self._alfabet)

    def find_alfabet(self):
        alfbt = []
        for state in self.get_states():
            for symbols in state.get_symbols():
                if symbols not in alfbt:
                    alfbt.append(symbols)
        return alfbt

    def get_states(self):
        return deepcopy(self._states)

    # def get_goalstates(self):
    #     return self._goalstates

    def __str__(self):
        string_res = ""

        for s in self._states:
            string_res += ("GOAL "if self.is_goal(s.get_state_name()) else "")+ str(s)

        return string_res




    def get_start_state(self):
        return copy(self._startstate)

    def is_goal(self,state_name):
        if type(state_name) == State:
            return state_name.get_state_name() in [g.get_state_name() for g in self._goalstates]
        return state_name in [g.get_state_name() for g in self._goalstates]

    def get_goal_states(self):
        return deepcopy(self._goalstates)



from default.state import EP
class NFA(StateMachine):

    class Builder(StateMachine.Builder):

        def build(self):
            if type(self.check_all()) == list:
                raise Exception(self.check_all())
            return NFA(self._startstate.get_state_name(),
                       self._states,
                       [g.get_state_name() for g in self._goalstates],
                       self._alfabet)

    def __init__(self, start_state_name, states, goal_states_name, alfabet=None):
        super().__init__(start_state_name, states, goal_states_name, alfabet)

    def move(self,states, in_symbol):
        res = []
        if type(states) == State:
            res.clear()
            for sym in states.get_symbols():
                if sym == in_symbol:
                    if type(states.get_child(sym)) == list:
                        for s in states.get_child(sym):
                            if not StateMachine.is_state_exist(s, res):
                                res.append(self.get_state_by_name(s))
                    else:
                        if not StateMachine.is_state_exist(states.get_child(sym),res):
                            res.append(self.get_state_by_name(states.get_child(sym)))


        elif type(states) == list:
            res.clear()
            for s in states:
                s_res = self.move(s, in_symbol)
                for sr in s_res:
                    if not StateMachine.is_state_exist(sr, res):
                        res.append(sr)
        else:
            raise TypeError( "move func error2!")

        return res

    def ep_closure1(self,states,on_explore=[]):
        res = []
        if states in res: return [states]
        if type(states) == State:
            res.clear()
            print(type(states),states.get_state_name())
            res.append(states)
            # on_explore.append(states)
            ep_res = self.move(states, EP)
            # print("ep res", [x.get_state_name() for x in ep_res])
            if len(ep_res) != 0:

                for s in ep_res:
                    if not self.is_state_exist(s,res):
                        res.append(s)
                        # print('res',res)
                        # print('s',s.get_state_name())
                        for i in self.ep_closure1(s,on_explore):
                            # print('\ti', i)
                            if not self.is_state_exist(i, res):
                                res.append(i)
            return res

        elif type(states) == list:
            res.clear()
            for s in states:
                s_res = self.ep_closure1(s)
                for sr in s_res:
                    if not self.is_state_exist(sr, res):
                        res.append(sr)
        else:
            raise TypeError( "move func error2!")

        return res

    def ep_closure(self,states):
        if type(states) not in [ list,State]:
            raise TypeError("move func error2!")
        from default.state import intersection_list,union_list
        res = states if type(states)==list else [states]
        ep_move = self.move(states,EP)
        res = union_list(ep_move, res)
        # print("initial ep_move",(ep_move))
        # print("initial res",(res))
        while True:
            # print("inters...",hash_state_list(intersection_list(res,ep_move)))
            ep_move = self.move(ep_move,EP)
            res = union_list(ep_move,res)
            # print("res", hash_state_list(res))
            # print("ep_move", hash_state_list(ep_move))
            if (union_list(res, ep_move)) == res: return res






class DFA(StateMachine):


    class Builder(StateMachine.Builder):

        def check_all(self):
            res =  super().check_all()

            alfabet_ep = False
            for s in self._states:
                if EP in s.get_symbols():
                    alfabet_ep = True
            if alfabet_ep:
                if type(res) == list:
                    res.append('ep-states')
                else:
                    res = ['ep-states']

            if self._alfabet not in [None,[]]:
                if EP in self._alfabet:
                    if type(res)==list:
                        res.append('ep-alfabets')
                    else: res = ['ep-alfabets']
                alfabet_matched = True
                for s in self._states:
                    if s.get_symbols() != self._alfabet:
                        alfabet_matched = False
                if not alfabet_matched:
                    if type(res)==list:
                        res.append('states-alfabets')
                    else: res = ['states-alfabets']
            return res

        def set_alfabet(self, alfabet):
            if EP in alfabet:
                raise ValueError("DFA have not EPSILON symbol")
            super().set_alfabet(alfabet)

        def build(self):
            if type(self.check_all()) == list:
                raise Exception(self.check_all())
            return DFA(self._startstate.get_state_name(),
                       self._states,
                       [g.get_state_name() for g in self._goalstates],
                       self._alfabet)

    def __init__(self, start_state_name, states, goal_states_name, alfabet=None):
        super().__init__(start_state_name, states, goal_states_name, alfabet)

    def move(self,states, in_symbol):
        res = []
        if type(states) == State:
            res.clear()
            for sym in states.get_symbols():
                if sym == in_symbol:
                    if type(states.get_child(sym)) == list:
                        for s in states.get_child(sym):
                            if not self.is_state_exist(s, res):
                                res.append(self.get_state_by_name(s))
                    else:
                        if not self.is_state_exist(states.get_child(sym),res):
                            res.append(self.get_state_by_name(states.get_child(sym)))


        elif type(states) == list:
            res.clear()
            for s in states:
                s_res = self.move(s, in_symbol)
                for sr in s_res:
                    if not StateMachine.is_state_exist(sr, res):
                        res.append(sr)
        else:
            raise TypeError( "move func error2!")

        return res

"""
graph.py

Created by Mohammadamin Tehrani
1/16/2019

"""

EP = 'epsilon'

class State:
    _childs = {}
    def __init__(self,name,childs=None):
        if childs is not None:
            if type(childs) != dict : raise (TypeError,"State constructor error1!")
            for c in childs:
                # if type(childs[c]) not in [State,list]: raise (TypeError,"State constructor error2!")
                if type(childs[c]) == list:
                    for s in c:
                        if type(childs) != State : raise (TypeError,"State constructor error3!");

        self._name = name
        self._childs = childs

    def to_tuple(self):
        return self._name,self._childs

    def get_child(self,symbol):
        for c in self._childs:
            if c==symbol: return self._childs[c]
        return None

    def get_childs(self):
        return self._childs




"""
graph.py

Created by Mohammadamin Tehrani
1/16/2019

"""

EP = 'epsilon'

class State:
    _childs = {}
    def __init__(self,name,childs={}):
        if len(childs)>0:
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

    def get_symbols(self):
        return [s for s in self._childs]

    def get_childs(self):
        return self._childs

    def __str__(self):
        # return self._name+" => "+str(self._childs)
        str_res = ""
        for c in self._childs:
            str_res+= self._name + " --"+c+"--> " + self._childs[c] +'\n'
        return str_res


    def get_state_name(self):
        return self._name


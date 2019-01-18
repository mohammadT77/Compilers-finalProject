"""
graph.py

Created by Mohammadamin Tehrani
1/16/2019

"""

EP = 'epsilon'

from copy import copy,deepcopy

class State:
    _childs = {}
    def __init__(self,name,childs={}):
        if len(childs)>0:
            if type(childs) != dict : raise (TypeError,"State constructor error1!")
            # for c in childs:
                # if type(childs[c]) not in [State,list]: raise (TypeError,"State constructor error2!")
                # if type(childs[c]) == list:
                #     for s in c:
                #         if type(childs) != State : raise (TypeError,"State constructor error3!");

        self._name = name
        self._childs = childs

    def to_tuple(self):
        return self.get_state_name(),self.get_childs()

    def get_child(self,symbol):
        for c in self._childs:
            if c==symbol: return deepcopy(self._childs[c])
        return None

    def __eq__(self, other):
        return type(other) == State and\
            other.get_state_name() == self.get_state_name() and\
            self.get_childs() == other.get_childs()

    def __le__(self, other):
        return self.get_state_name()<=other.get_state_name()
    def __lt__(self, other):
        return self.get_state_name()<other.get_state_name()


    def __gt__(self, other):
        return self.get_state_name()>other.get_state_name()
    def __ge__(self, other):
        return self.get_state_name()>=other.get_state_name()

    def get_symbols(self):
        return [copy(s) for s in self._childs]

    def get_childs(self):
        return deepcopy(self._childs)

    def __str__(self):
        # return self._name+" => "+str(self._childs)
        str_res = ""
        for c in self._childs:
            str_res+= self._name + " --"+c+"--> " + str(self._childs[c]) +'\n'
        if str_res == "" : str_res=self._name+"\n"
        return str_res


    def get_state_name(self):
        return copy(self._name)



def hash_state_list(states):
    if type(states) != list and type(states[0]) != State:
        raise Exception
    res = ""
    states.sort()
    for x in states:
        res+=x.get_state_name()+"|"
    return res[0:-1]


def intersection_list(l1,l2):
    if type(l1) != list or type(l2)!=list:
        raise Exception("UNION LIST argument not list")
    res = []
    for i in l1:
        if i in l2: res.append(i)

    return deepcopy(res)


def union_list(l1,l2):
    if type(l1) != list or type(l2)!=list:
        raise Exception("UNION LIST argument not list")
    res = l1+l2
    for i in intersection_list(l1,l2):
        res.remove(i)

    return deepcopy(res)


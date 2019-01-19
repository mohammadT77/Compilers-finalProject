from default.state_machines import NFA,DFA,State,NFA_to_DFA_convertor,EP


def text_from_file(file_path):
    try:
        file = open(file_path,'r')
    except IOError:
        raise Exception("Could not Open file("+str(file_path)+")")
    text = str(file.read())
    file.close()
    return text

def save_file(path,text):
    try:
        file = open(path,'w')
    except IOError:
        raise Exception("Could not Open file("+str(path)+")")
    file.write(text)
    file.close()
    return text



def find_regex_in_text_by_dfa(dfa,in_text):
    if type(dfa) != DFA :raise Exception("Invalid DFA argument type")
    if type(in_text) != str :raise Exception("Invalid IN_STRING argument type")
    res = []
    def __get_words():
        return str.split(in_text)
    for w in __get_words():
        if match_string_by_dfa(dfa,w):
            res.append(w)
    return res


def match_string_by_dfa(dfa,in_string):
    if type(dfa) != DFA :raise Exception("Invalid DFA argument type")
    if type(in_string) != str :raise Exception("Invalid IN_STRING argument type")

    def __in_token(string):
        buffer =""
        res = []
        for c in string:
            buffer+=c
            if buffer in dfa.get_alfabet():
                res.append(buffer)
                buffer=""
        if len(buffer)!=0 :
            return res +[buffer,]
        return res

    curr_state = dfa.get_start_state()
    # print(__in_token(in_string)) #TODO Trace
    for c in __in_token(in_string):
        curr_state = dfa.move(curr_state,c)
        if curr_state is None:return False
        if type(curr_state) != State:
            type_ = type(curr_state)
            raise Exception("Unexcepted type!!"+str(type_)+":"+str(curr_state))
        elif curr_state.get_state_name()=='DS': return False
    if dfa.is_goal(curr_state): return True


from tests.some_nfa import nfa_figure3_26
# from tests.some_nfa import nfa_real_number_regex
# dfa = NFA_to_DFA_convertor(nfa_real_number_regex())
# text = "123 23 sdf 2 sdf 1241 dsa23 sd 1.231"
# print(find_regex_in_text_by_dfa(dfa,text))
# print(match_string_by_dfa(NFA_to_DFA_convertor(nfa_real_number_regex()),'123.123E+2'))
# print(text_from_file("C:\\Users\\Mohammad Amin\\Desktop\\asda.txt"))
# print(save_file("C:\\Users\\Mohammad Amin\\Desktop\\Aasda.txt","""123
# 1231
# 31efw"""))
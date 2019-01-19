from default.state_machines import NFA,DFA,State,EP
from default.state_machines import NFA_to_DFA_convertor as nfa_convertor
from tests.some_nfa import nfa_real_number_regex
from default.text_processing import *


def main(args_v):
    text = ""
    save_path = "last_output.txt"
    if len(args_v) >3:
        print("invalid argv!!!")
        exit()
    elif len(args_v) == 3:
        print("File Path:", args_v[1])
        print("Save Path:", args_v[2])
        text = text_from_file(args_v[1])
        save_path = args_v[2]
    elif len(args_v) == 2:
        print("File Path:",args_v[1])
        text = text_from_file(args_v[1])
    else:
        text = input("Enter your Text: ")

    print("------------------------------------------------------\nINPUT TEXT:")
    for l in str.splitlines(text):
        print("-",l)

    print("------------------------------------------------------\nRegExr: (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?\n------------------------------------------------------")

    nfa = nfa_real_number_regex()
    dfa = nfa_convertor(nfa)

    print("NFA:\n",nfa,"\n-------------------------------------------------------")
    print("DFA:\n",dfa,"\n")

    output = find_regex_in_text_by_dfa(dfa,text)
    print("======================================================\nOUTPUT:")
    string_output = ""
    for i in range(len(output)):
        string_output += str(i+1)+")"+output[i]+"\n"
    print(string_output)
    print("======================================================")
    print("Save Path:",save_path)
    save_file(save_path,string_output)
    print("Saved!")




import sys
main(sys.argv)
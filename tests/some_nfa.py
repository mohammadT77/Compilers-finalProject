from default.state_machines import NFA,State,EP



def nfa_real_number_regex():

    """
    :returns NFA of regex:
        regex:    (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?
    """
    class alfabet:
        d = [str(i) for i in range(10)]
        e = 'e'
        E = 'E'
        plus = '+'
        minus = '-'
        dot = '.'
        EP = EP

        @staticmethod
        def to_array():
            return alfabet.d+[alfabet.e,alfabet.E,alfabet.plus,alfabet.minus,alfabet.dot,alfabet.EP]

    state = [
        State('start',{
            EP:['1','3','6']
        }),
        State('1',{
            alfabet.d[0]:'2',
            alfabet.d[1]:'2',
            alfabet.d[2]:'2',
            alfabet.d[3]:'2',
            alfabet.d[4]:'2',
            alfabet.d[5]:'2',
            alfabet.d[6]:'2',
            alfabet.d[7]:'2',
            alfabet.d[8]:'2',
            alfabet.d[9]:'2'
        }),
        State('2', {
            EP: ['1','3']
        }),
        State('3', {
            EP: '4'
        }),
        State('4', {
            alfabet.dot:'5'
        }),
        State('5', {
            EP: '6'
        }),
        State('6', {
            EP: '7'
        }),
        State('7', {
            alfabet.d[0]: '8',
            alfabet.d[1]: '8',
            alfabet.d[2]: '8',
            alfabet.d[3]: '8',
            alfabet.d[4]: '8',
            alfabet.d[5]: '8',
            alfabet.d[6]: '8',
            alfabet.d[7]: '8',
            alfabet.d[8]: '8',
            alfabet.d[9]: '8'
        }),
        State('8', {
            EP : ['7','9','end']
        }),
        State('9', {
            EP : ['10','12']
        }),
        State('10', {
            alfabet.e : '11'
        }),
        State('11', {
            EP : '14'
        }),
        State('12', {
            alfabet.E : '13'
        }),
        State('13', {
            EP : '14'
        }),
        State('14', {
            EP : ['15','17','19']
        }),
        State('15', {
            alfabet.minus : '16'
        }),
        State('16', {
            EP : '19'
        }),
        State('17', {
            alfabet.plus : '18'
        }),
        State('18', {
            EP : '19'
        }),
        State('19', {
            EP : '20'
        }),
        State('20', {
            alfabet.d[0]: '21',
            alfabet.d[1]: '21',
            alfabet.d[2]: '21',
            alfabet.d[3]: '21',
            alfabet.d[4]: '21',
            alfabet.d[5]: '21',
            alfabet.d[6]: '21',
            alfabet.d[7]: '21',
            alfabet.d[8]: '21',
            alfabet.d[9]: '21'
        }),
        State('21', {
            EP : ['20','end']
        }),
        State('end', {})
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_alfabet(alfabet.to_array())
    nfa_builder.set_startstate(state[0])
    for s in state[1:-1]:
        nfa_builder.add_state(s)
    nfa_builder.add_state(state[-1],True)

    nfa = nfa_builder.build()
    return nfa

nfa_real_number_regex()

def nfa_real_number_regex_demo():

    """
    :returns NFA of regex:
        regex:    (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?
        euqals:   (( (\d)+ )?\.)? (\d)+ ([eE][-+]?(\d)+)?
    """
    class alfabet:
        d = '\d'
        e = 'e'
        E = 'E'
        plus = '+'
        minus = '-'
        dot = '\.'
        EP = EP

        @staticmethod
        def to_array():
            return ['\d','e','E','+','-','\.',EP]


    state = [
        State('start',{
            EP:['1','3','6']
        }),
        State('1',{
            alfabet.d:'2'
        }),
        State('2', {
            EP: ['1','3']
        }),
        State('3', {
            EP: '4'
        }),
        State('4', {
            alfabet.dot:'5'
        }),
        State('5', {
            EP: '6'
        }),
        State('6', {
            EP: '7'
        }),
        State('7', {
            alfabet.d : '8'
        }),
        State('8', {
            EP : ['7','9','end']
        }),
        State('9', {
            EP : ['10','12']
        }),
        State('10', {
            alfabet.e : '11'
        }),
        State('11', {
            EP : '14'
        }),
        State('12', {
            alfabet.E : '13'
        }),
        State('13', {
            EP : '14'
        }),
        State('14', {
            EP : ['15','17','19']
        }),
        State('15', {
            alfabet.minus : '16'
        }),
        State('16', {
            EP : '19'
        }),
        State('17', {
            alfabet.plus : '18'
        }),
        State('18', {
            EP : '19'
        }),
        State('19', {
            EP : '20'
        }),
        State('20', {
            alfabet.d : '21'
        }),
        State('21', {
            EP : ['20','end']
        }),
        State('end', {})
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_alfabet(alfabet.to_array())
    nfa_builder.set_startstate(state[0])
    for s in state[1:-1]:
        nfa_builder.add_state(s)
    nfa_builder.add_state(state[-1],True)

    nfa = nfa_builder.build()
    return nfa


# print(nfa_real_number_regex())



def nfa_exercise3_6_4():
    # Exercise 3.6.4 of Compiler book
    state = [
        State('0',{'a':'1',EP:'3'}),
        State('1',{'b':'2',EP:'0'}),
        State('2',{'b':'3',EP:'1'}),
        State('3',{'a':'0',EP:'2'}),
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_startstate(state[0])
    nfa_builder.add_state(state[1])
    nfa_builder.add_state(state[2])
    nfa_builder.add_state(state[3],True)
    return nfa_builder.build()

def nfa_figure3_26():
    # Exercise 3.6.4 of Compiler book
    state = [
        State('0',{EP:['1','3']}),
        State('1',{'a':'2'}),
        State('2',{'a':'2'}),
        State('3',{'b':'4'}),
        State('4',{'b':'4'}),
    ]
    nfa_builder = NFA.Builder()
    nfa_builder.set_startstate(state[0])
    nfa_builder.add_state(state[1])
    nfa_builder.add_state(state[2],True)
    nfa_builder.add_state(state[3])
    nfa_builder.add_state(state[4],True)
    return nfa_builder.build()


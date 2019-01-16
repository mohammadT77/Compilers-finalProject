from default.state import State,EP



childs = {
    'a': 'A',
    EP : 'E',
    'b': 'B'
}

s1 = State('S', childs)
print(s1.get_symbols())
print(s1.get_child('a'))
print(s1.get_childs())
print(s1.get_state_name())
print(s1.to_tuple())
print(s1)


assert (s1.get_symbols() == ['a', EP, 'b']) , s1.get_symbols()
assert s1.get_child('a'), "get_childs!!!"
assert (s1.get_state_name() == 'S'), "get_state_name !!!"

print("------S2--------")

s2  = State('S')
print(s2.get_symbols())
print(s2.get_child('a'))
print(s2.get_childs())
print(s2.get_state_name())
print(s2)

print('\n\nOK')



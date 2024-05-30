my_dict = {'Ivan': 1990, 'Petr': 1989, 'Mariya': 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Petr'))
print('Not existing value:', my_dict.get('Vasya'))
my_dict.update({"Sasha": 1961,
                'Viktor': 1956})
a = my_dict.pop('Mariya')
print('Delete value:', a)
print('Modified dict:', my_dict)

my_set = {1,2,3,3,2,1,'OK','OK'}
print('Set:', my_set)
my_set.add(5)
my_set.add('Bad')
my_set.discard(2)
print('Modified set:', my_set)
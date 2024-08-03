my_dict = {'Daniil': 2012, 'Vasiliy': 2017, 'Nikolay': 1986}
print('Dict:', my_dict)
print('Existing value:', my_dict['Daniil'])
print('Not existing value:', my_dict.get('Elena'))
my_dict.update({'Kseniya': 2001,
                'Alexsandr': 1968})
Vasiliy = my_dict.pop('Vasiliy')
print('Deleted value:', Vasiliy)
print('Modified dictionary:', my_dict)

my_set = {4, 5, 6, 6, 4, 'Vika', 'Sonya', 'Vika', 1, 5}
print('Set:', my_set)
my_set.update({45, 'Tanya'})
my_set.discard('Vika')
print('Modified set:', my_set)
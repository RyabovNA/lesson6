my_dict = {'Daniil': 2012, 'Vasiliy': 2017, 'Nikolay': 1986}
print(my_dict)
print(my_dict['Daniil'])
my_dict['Elena'] = 1988
print(my_dict['Elena'])
my_dict.update({'Kseniya': 2001,
                'Alexsandr': 1968})
Vasiliy = my_dict.pop('Vasiliy')
print(Vasiliy)
print(my_dict)

my_set = {4, 5, 6, 6, 4, 'Vika', 'Sonya', 'Vika', 1, 5}
print('Set:', my_set)
my_set.update({45, 'Tanya'})
my_set.discard('Vika')
print('Modified set:', my_set)
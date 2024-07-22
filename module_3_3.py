def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])
print()
values_list = [11, False, 'qwerty']
values_dict = {'a': 8, 'b': True, 'c': 'QWERTY'}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [888888888, 'СтРоКа']
print_params(*values_list_2, 123456789)
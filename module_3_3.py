def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params("Hello")
print()

values_list = [3, 'Ilya', False]
value_dist = {'a': 4, 'b': 'Elena', 'c': True}
print_params(*values_list)
print_params(**value_dist)
values_list2 = [3, 'Valeriya']
print_params(*values_list2, 42)

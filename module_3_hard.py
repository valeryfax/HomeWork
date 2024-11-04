data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    all_summ = 0
    for i in args:
        if isinstance(i, (list, tuple, set)):
            all_summ += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            all_summ += calculate_structure_sum(*i.items())
        elif isinstance(i, str):
            all_summ += len(i)
        elif isinstance(i, (int, float)):
            all_summ += i
    return all_summ


result = calculate_structure_sum(data_structure)

print(result)

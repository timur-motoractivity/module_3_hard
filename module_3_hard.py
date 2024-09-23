

data_structure = [
    [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_nested_sum(*args):
    total = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)): # функция isinstance для определения типа данного
            total += calculate_nested_sum(*arg)
        elif isinstance(arg, dict):
            total += calculate_nested_sum(*arg.items())
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, (int, float)):
            total += arg
    return total
result = calculate_nested_sum(data_structure)
print(result)
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def perebor ():

  for a in data_structure:
    if isinstance(a, list):
      for a1 in a:
        print(a1)
  for b in data_structure:
    if isinstance(b, dict):
      for b1 in b:
        print(b1)
  for c in data_structure:
    if isinstance(c, str):
      print(len(c))
  for d in data_structure:
    if isinstance(d, tuple):
      for d1 in d:
        print(d1)


perebor()

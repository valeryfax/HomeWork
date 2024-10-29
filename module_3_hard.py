data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def perebor ():
    spisok = []
    for a in data_structure:
        if isinstance(a, list):
            for a1 in a:
                spisok.append(a1)
        if isinstance(a, dict):
            for b1 in a.keys():
                spisok.append (len(b1))
            for b1 in a.values():
                spisok.append (b1)
        if isinstance(a, tuple):
            for c1 in a:
                if isinstance(c1, int):
                    spisok.append(c1)
                if isinstance(c1, dict):
                    for c2 in c1.keys():
                        spisok.append (len(c2))
                    for c2 in c1.values():
                        spisok.append (c2)
                
        if isinstance(a, str):
            spisok.append (len(a))
    for c3 in a:
        for c4 in c3:
            for c5 in c4:
                for c6 in c5:
                    if isinstance(c6, int):
                        spisok.append(c6)
                    if isinstance(c6, str):
                        spisok.append (len(c6))    
                    if isinstance(c6, tuple):
                        for c7 in c6:
                            if isinstance(c7, str):
                                spisok.append (len(c7))
                            if isinstance(c7, int):
                                spisok.append(c7)
    print(sum(spisok))
    
perebor()





def count_calls():
    global calls
    calls = calls + 1


def string_info():
    global stroka
    print(f' {len(stroka)}, {stroka.upper()}, {stroka.lower()}')
    count_calls()


def is_contains():
    global string
    count_calls()
    list_to_search = ["ПЕРВЫЙ", "ВТОРОЙ", "ТРЕТИЙ"]
    if string in list_to_search:
        n = True
    else:
        n = False
    print(n)

calls = 0
while 1>0:
    stroka = input("Введите строку: ")
    string = (input("Введите строку: ").upper())
    string_info ()
    is_contains()
    print(calls)

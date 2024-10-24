def get_multiplied_digits (number):
    str_number = str(number) # 40203
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(1010101))
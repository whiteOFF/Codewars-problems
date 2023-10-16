def clean(st) -> str:
    if st.count('0') == len(st):
        return '0'
    counter = 0
    while st[counter] == '0':
        counter += 1
    return st[counter::]


# TROPPO LENTO CON STRINGHE TROPPO LUNGHE
# PS: int contiene numeri fino a 4399 cifre
def sum_strings2(x, y):
    x = clean(x)
    y = clean(y)
    max_length = (len(x) if len(x) >= len(y) else len(y))
    x = '0' * (max_length - len(x)) + x
    y = '0' * (max_length - len(y)) + y
    returning = ""
    rem = 0
    for i in range(max_length-1, -1, -1):
        add = rem + int(x[i]) + int(y[i])
        if add > 9:
            rem = 1
            returning = str(add)[1] + returning
        else:
            rem = 0
            returning = str(add) + returning
    if rem > 0:
        return str(rem) + returning
    if len(returning) == 0:
        return "0"
    if returning[0] == '0':
        return clean(returning)
    return returning


def sum_strings(x, y) -> str:
    spanning = 4299
    x = clean(x)
    y = clean(y)
    max_length = max(len(x), len(y))
    x = '0' * (max_length - len(x)) + x
    y = '0' * (max_length - len(y)) + y
    returning = ""
    rem = 0
    for i in range(max_length, -1, -spanning):
        add = rem + int(x[(i-spanning if i-spanning >= 0 else 0):i]) + int(y[(i-spanning if i-spanning >= 0 else 0):i])
        add_str = str(add)
        if len(add_str) > spanning:
            rem = 1
            returning = add_str[1::] + returning
        else:
            rem = 0
            returning = add_str + returning
    if rem > 0:
        return str(rem) + returning
    if len(returning) == 0:
        return "0"
    if returning[0] == '0':
        return clean(returning)
    return returning


print(sum_strings2("623", "623"))
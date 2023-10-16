'''
"X O X X O"
"O X X O X"
"O O O X X"
"O O O O X"
"O O O O O"
'''


def land_perimeter(arr):
    string, ln_len = "".join(arr), len(arr[0])
    perimeter = 4 * string.count('X')
    for i in range(ln_len):
        for j in range(len(arr) - 1):
            if string[i + ln_len * j] == 'X' and string[i + ln_len * (j + 1)] == 'X':
                perimeter -= 2
    for i in range(len(arr)):
        for j in range(ln_len-1):
            if string[ln_len * i + j] == 'X' and string[ln_len * i + j + 1] == 'X':
                perimeter -= 2
    return f"Total land perimeter: {perimeter}"


lista = ['XOOO',
         'XOXO',
         'XOXO',
         'OOXX',
         'OOOO']

print(land_perimeter(lista))

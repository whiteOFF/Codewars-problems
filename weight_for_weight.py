''' my original code
def order_weight(str):
    return " ".join([str(n) for n in sorted(str.split(sep=' '), key=lambda word: sum(int(word[i]) + int(word[i])/10/(10**i) if int(word[i]) != 0 else 1/100/(10**i) for i in range(len(word))))])
'''


# renewed
def order_weight(_str):
    return " ".join([str(n) for n in sorted(sorted(_str.split()), key=lambda word: sum(int(i) for i in word))])



a = "12 43 200 11 20 110000"
print(order_weight(a))

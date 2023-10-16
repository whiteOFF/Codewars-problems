import math


def postfix_evaluator(expr):
    def modify(lista, i, res):
        new = []
        for x in range(i):
            new.append(lista[x])
        new.append(res)
        x = i + 3
        while x < len(lista):
            new.append(lista[x])
            x += 1
        return new

    def pe(lista):
        if len(lista) == 1:
            return int(lista[0])
        i = 2
        while True:
            if lista[i] == '+':
                result = int(lista[i - 2]) + int(lista[i - 1])
                return pe(modify(lista, i - 2, result))
            elif lista[i] == '-':
                result = int(lista[i - 2]) - int(lista[i - 1])
                return pe(modify(lista, i - 2, result))
            elif lista[i] == '*':
                result = int(lista[i - 2]) * int(lista[i - 1])
                return pe(modify(lista, i - 2, result))
            elif lista[i] == '/':
                result = math.floor(float(lista[i - 2]) / float(lista[i - 1]))
                return pe(modify(lista, i - 2, result))
            else:
                i += 1

    lista = expr.split()
    return pe(lista)


print(postfix_evaluator("49 -5 / 16 *"))
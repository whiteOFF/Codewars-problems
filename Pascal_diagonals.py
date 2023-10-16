def generate_diagonal(n, l):
    def pascal(line):
        result = [[1]]
        if line == 0:
            return result[0]
        i = 0
        while i < line:
            appending = []
            for j in range(len(result[i]) - 1):
                appending.append(result[i][j] + result[i][j + 1])
            appending.insert(0, 1)
            appending.append(1)
            result.append(appending)
            i += 1
        return result[i]

    lista = []
    if l == 0: return lista
    for i in range(l):
        lista.append(pascal(n + i)[i])
    return lista

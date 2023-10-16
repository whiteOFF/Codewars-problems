def to_underscore(string):
    strn = str(string)
    uppers = "QWERTYUIOPASDFGHJKLZXCVBNM"
    result = strn[0].lower()
    for i in range(1, len(strn)):
        if strn[i] in uppers:
            result += '_' + strn[i].lower()
        else: result += strn[i]
    return result


print(to_underscore("Pascal3Notazio"))
def high(x):
    word_list = x.split(sep=' ')
    best_word = word_list.pop(0)
    best_value = 0
    for char in best_word:
        best_value += ord(char) - ord('a') + 1

    for current_word in word_list:
        current_value = 0
        for char in current_word:
            current_value += ord(char) - ord('a') + 1
        if current_value > best_value:
            best_value = current_value
            best_word = current_word

    return best_word










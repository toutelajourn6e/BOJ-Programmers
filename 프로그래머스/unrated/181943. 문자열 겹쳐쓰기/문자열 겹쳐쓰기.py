def solution(my_string, over, s):
    my_string = list(my_string)
    for i, c in zip(range(s, len(over) + s), over):
        my_string[i] = c
    return ''.join(my_string)
def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string): return 0
    for i, j in zip(my_string, is_prefix):
        if i != j: return 0
    return 1
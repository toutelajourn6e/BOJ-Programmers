def solution(a, b):
    foo = int(str(a) + str(b))
    bar = int(str(b) + str(a))
    return foo if foo > bar else bar
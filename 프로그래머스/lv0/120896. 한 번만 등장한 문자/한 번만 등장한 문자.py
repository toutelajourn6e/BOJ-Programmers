def solution(s):
    answer = dict()
    my_string = list()
    for i in s:
        if not i in answer:
            answer[i] = 0
            answer[i] += 1
        else:
            answer[i] += 1
        
    for j in answer:
        if answer[j] != 1:
            pass
        else:
            my_string.append(j)
    my_string.sort()
    
    return ''.join(my_string)
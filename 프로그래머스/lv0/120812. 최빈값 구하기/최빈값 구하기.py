from collections import Counter

def solution(array):
    if sum(array) / len(array) == array[0]:
        return array[0]
        
    count = Counter(array)
    mode = count.most_common(2)
    
    if mode[0][1] == mode[1][1]:
        return -1
    else:
        return mode[0][0]
        
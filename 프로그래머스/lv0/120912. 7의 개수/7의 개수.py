def solution(array):
    answer = 0
    
    for i in array:
        i = str(i)
        i = ' '.join(i).split()
        for j in i:
            if '7' in i:
                while '7' in i:
                    i.remove('7')
                    answer += 1
    return answer
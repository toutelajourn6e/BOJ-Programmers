def solution(s):
    answer = list()
    
    for i in s.split():
        try:
            answer.append(int(i))
        except:
            del answer[-1]
    
    return sum(answer)

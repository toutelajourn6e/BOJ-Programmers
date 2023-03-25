def solution(emergency):
    re = sorted(emergency, reverse=True)
    answer = emergency.copy()
    
    for index, i in enumerate(re):
        findint = answer.index(i)
        emergency[findint] = index+1
    return emergency
        

from collections import defaultdict

def solution(participant, completion):
    person = defaultdict(int)
    
    for i in participant:
        person[i] += 1
        
    for i in completion:
        person[i] -= 1
        
    for i in person:
        if person[i] == 1:
            return i
    
    
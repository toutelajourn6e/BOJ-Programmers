from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    ans = []
    people = defaultdict(list)
    
    for i in info:
        applicant = i.split()
        score = int(applicant.pop())
        people[''.join(applicant)].append(score)
        
        for j in range(4):
            candi = list(combinations(applicant, j))
            for c in candi:
                people[''.join(c)].append(score)
                
    for i in people:
        people[i].sort()
        
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        ans.append(len(people[key]) - bisect_left(people[key], score))
        
    return ans
        
            
        
        
        
    
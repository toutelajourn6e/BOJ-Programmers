from itertools import combinations
from collections import defaultdict
import re

def solution(orders, course):
    menu = defaultdict(int)
    result = []
    
    for i in course:
        for j in orders:
            if len(j) >= i:
                for k in list(combinations(sorted(j), i)):
                    menu[''.join(k)] += 1
    
    max_v = [0] * (max(course)+1)
    for i in course:
        for key, val in menu.items():
            if val > 1 and len(key) == i and val > max_v[i]:
                max_v[i] = val
        
    for i in course:
        for key, val in menu.items():
            if val > 1 and len(key) == i and val == max_v[i]:
                result.append(key)
                
    return sorted(result)
            
        
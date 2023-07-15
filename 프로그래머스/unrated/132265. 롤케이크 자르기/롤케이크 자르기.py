from collections import defaultdict

def solution(topping):
    chulsu = {}
    brother = {}
    ans = 0
    
    for i in topping:
        brother[i] = brother.get(i, 0) + 1
        
    for i in topping:
        chulsu[i] = chulsu.get(i, 0) + 1
        if brother[i] == 1: del brother[i]
        else: brother[i] -= 1
        
        if len(chulsu) == len(brother):
            ans += 1
            
    return ans
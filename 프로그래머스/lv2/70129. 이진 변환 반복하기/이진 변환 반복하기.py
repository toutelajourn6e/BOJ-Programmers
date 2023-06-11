def solution(s):
    ans = [0,0]
    
    while s != '1':
        before = len(s)
        
        s = s.replace('0', '')
        ans[0] += 1
        
        after = len(s)
        
        ans[1] += (before - after)
        s = bin(after)[2:]
    return ans  
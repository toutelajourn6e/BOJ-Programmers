def check(wants):
    for i in wants:
        if wants[i] > 0:
            return False
    return True


def solution(want, number, discount):
    wants = {}
    ans = 0
    
    for w, n in zip(want, number):
        wants[w] = n
        
    for i in range(10):
        if discount[i] in wants:
            wants[discount[i]] -= 1
    
    if check(wants): ans += 1

    for i in range(10, len(discount)):
        if discount[i] in wants:
            wants[discount[i]] -= 1
        if discount[i-10] in wants:
            wants[discount[i-10]] += 1
        
        if check(wants): ans += 1
    
    return ans
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    ans = [0, 0]
    
    gcd_a = arrayA[0]
    for i in range(1, len(arrayA)):
        if gcd_a <= 1: break
        gcd_a = gcd(gcd_a, arrayA[i])
        
    gcd_b = arrayB[0]
    for i in range(1, len(arrayB)):
        if gcd_b <= 1: break
        gcd_b = gcd(gcd_b, arrayB[i])
        

    if gcd_a >= 1:
        for i in arrayB:
            if not i % gcd_a: break
        else: ans[0] = gcd_a

    if gcd_b >= 1:
        for i in arrayA:
            if not i % gcd_b: break
        else: ans[1] = gcd_b
        
    return max(ans)
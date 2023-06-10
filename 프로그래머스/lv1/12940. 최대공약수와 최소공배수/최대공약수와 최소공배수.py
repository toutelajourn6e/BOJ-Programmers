def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a, b, gcd):
    return a * b // gcd

def solution(n, m):
    result = []
    
    gcd = get_gcd(n, m)
    lcm = get_lcm(n, m, gcd)
    
    result.append(gcd)
    result.append(lcm)
    
    return result
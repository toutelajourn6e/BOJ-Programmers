a, b = map(int,input().split())
def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a%b)
    
gcd = get_gcd(a, b)

print(gcd)
print((a*b)//gcd)
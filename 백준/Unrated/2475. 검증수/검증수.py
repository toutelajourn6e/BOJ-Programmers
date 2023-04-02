a, b, c, d, e = map(int, input().split())

def arith(A, B, C, D, E):
    print(((A**2)+(B**2)+(C**2)+(D**2)+(E**2))%10)

arith(a, b, c, d, e)
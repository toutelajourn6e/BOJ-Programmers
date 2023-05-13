from fractions import Fraction

def solution(a, b):
    f = Fraction(a, b)
    a = f.numerator
    b = f.denominator
    if a % b == 0:
        return 1

    prime = set()
    num = 2
    while b != 1:
        if b % num == 0:
            b //= num
            prime.add(num)
        else:
            num += 1
            
    if prime == {2,5} or prime == {2} or prime == {5}: return 1
    else: return 2
    
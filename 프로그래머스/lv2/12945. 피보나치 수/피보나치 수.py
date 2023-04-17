def solution(n):
    a = 1
    b = 1
    for _ in range(1,n):
        a, b = b, a + b
    return a % 1234567
    
def solution(n):
    return sum([i for i in range(1, n+1, 2)]) if n % 2 else sum([j*j for j in range(0, n+1, 2)])
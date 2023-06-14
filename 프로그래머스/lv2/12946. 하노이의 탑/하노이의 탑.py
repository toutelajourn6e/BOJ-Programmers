def hanoi(n, start, via, end, result):
    if n == 1:
        result.append([start, end])
        return
    
    hanoi(n-1, start, end, via, result)
    result.append([start, end])
    hanoi(n-1, via, start, end, result)

def solution(n):
    result = []
    hanoi(n, 1, 2, 3, result)
    return result
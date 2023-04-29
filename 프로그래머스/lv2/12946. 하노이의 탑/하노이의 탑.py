def solution(n):
    ans = []
    def hanoi(n, start=1, aux=2, end=3):
        if n == 1:
            ans.append([start, end])
            return
        
        hanoi(n-1, start, end, aux)
        
        ans.append([start, end])
        
        hanoi(n-1, aux, start, end)
    
    hanoi(n)
    return ans
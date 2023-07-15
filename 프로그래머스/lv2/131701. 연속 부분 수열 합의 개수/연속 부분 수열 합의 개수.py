def solution(elements):
    ans = set()
    circular = elements * 2
    
    for i in range(len(elements)):
        window = sum(circular[:i+1])
        ans.add(window)
        for j in range(i+1, len(circular)):
            window += circular[j]
            window -= circular[j-(i+1)]
            ans.add(window)
    return len(ans)
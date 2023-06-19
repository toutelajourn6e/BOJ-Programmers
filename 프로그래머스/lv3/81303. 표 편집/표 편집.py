import heapq as hq

def solution(n, k, cmd):
    left = []
    right= []
    deleted = []
    
    for i in range(n):
        hq.heappush(right, i)
    
    for _ in range(k):
        hq.heappush(left, -hq.heappop(right))
        
    
    for i in cmd:
        if len(i) > 1:
            act, cnt = i.split()
            if act == 'U':
                for _ in range(int(cnt)):
                    hq.heappush(right, -hq.heappop(left))

            if act == 'D':
                for _ in range(int(cnt)):
                    hq.heappush(left, -hq.heappop(right))
        
        else:
            if i == 'C':
                deleted.append(hq.heappop(right))
            if not right:
                hq.heappush(right, -hq.heappop(left))

            if i == 'Z':
                index = deleted.pop()
                if index > right[0]:
                    hq.heappush(right, index)
                else:
                    hq.heappush(left, -index)
                
    ans = ['O' for _ in range(n)]
    
    for i in deleted:
        ans[i] = 'X'

    return ''.join(ans)

    
from collections import deque

def solution(priorities, location):
    max_p = max(priorities)
    q = deque([(val, idx) for idx, val in enumerate(priorities)])
    cnt = 1

    while q:
        val, idx = q.popleft()
        if val == max_p:
            if idx == location:
                return cnt
            else:
                cnt += 1
                max_p = max(q)[0]
        else:
            q.append((val, idx))            
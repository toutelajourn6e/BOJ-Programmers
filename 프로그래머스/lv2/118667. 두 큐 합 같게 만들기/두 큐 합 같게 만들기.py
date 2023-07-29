from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    s_q1, s_q2 = sum(queue1), sum(queue2)
    median = (s_q1 + s_q2) // 2
    ans = 0
    
    while ans <= (len(queue1) + len(queue2)) * 2:
        if s_q1 > median:
            data = queue1.popleft()
            queue2.append(data)
            s_q1 -= data
            s_q2 += data
            ans += 1
        elif s_q1 < median:
            data = queue2.popleft()
            queue1.append(data)
            s_q1 += data
            s_q2 -= data
            ans += 1
        else: break
    else: return -1
    return ans
from collections import deque

def solution(number, k):
    number = list(number)
    left, right = deque(), deque(list(map(int, number)))

    cnt = 0
    while True:
        if cnt == k: break
        if not left: left.append(right.popleft())
        elif left[-1] < right[0]:
            left.pop()
            cnt += 1
        elif len(right) == 1:
            right.pop()
            break
        elif right[0] < right[1]:
            right.popleft()
            cnt += 1
        else: left.append(right.popleft())
    
    return ''.join(map(str, list(left) + list(right)))
    
            
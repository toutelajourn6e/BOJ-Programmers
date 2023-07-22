from collections import deque

def solution(order):
    boxes = deque([i for i in range(1, len(order)+1)])
    order = deque(order)
    stack = []
    ans = 0
    
    while boxes:
        if order[0] == boxes[0]:
            order.popleft()
            boxes.popleft()
            ans += 1
        elif stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            ans += 1
        else:
            stack.append(boxes.popleft())
            
    while stack:
        box = stack.pop()
        if box == order[0]:
            order.popleft()
            ans += 1
        else: break
    return ans    
from collections import deque

def solution(prices):
    n = len(prices)
    prices = deque(prices)
    stack = []
    result = [0] * len(prices)
    
    for i in range(n):
        price = prices.popleft()
        if not stack:
            stack.append((i, price))
        else:
            while stack:
                if stack[-1][1] <= price:
                    break
                else:
                    temp = stack.pop()
                    result[temp[0]] = i - temp[0] 
            stack.append((i, price))
            
    while stack:
        temp = stack.pop()
        result[temp[0]] = (n-1) - temp[0]
    
    return result
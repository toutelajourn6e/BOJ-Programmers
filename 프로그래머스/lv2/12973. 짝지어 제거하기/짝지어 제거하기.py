def solution(s):
    s = list(s)
    stack = [s.pop()]
    
    while True:
        if not s:
            if not stack: return 1
            else: return 0
        
        if not stack:
            stack.append(s.pop())
            continue
            
        if s[-1] == stack[-1]:
            s.pop()
            stack.pop()
        else:
            stack.append(s.pop())

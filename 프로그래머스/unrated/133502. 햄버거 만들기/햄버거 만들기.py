def solution(ingredient):
    ans = 0
    stack = []
    recipe = [1, 2 ,3 ,1]
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and sum(stack[-4:]) == 7:
            for s, r in zip(range(-4, 0, 1), recipe):
                if stack[s] != r:
                    break
            else:
                for _ in range(4):
                    stack.pop()
                ans += 1
                
    return ans
                
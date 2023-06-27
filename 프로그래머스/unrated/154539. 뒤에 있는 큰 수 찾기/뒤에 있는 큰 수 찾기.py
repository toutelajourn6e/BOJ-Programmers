def solution(numbers):
    n = len(numbers)
    stack = []
    ans = numbers[:]

    for i in range(n):
        if not stack:
            stack.append((numbers[i],i))
        elif stack and stack[-1][0] < numbers[i]:
            while stack:
                if stack[-1][0] >= numbers[i]:
                    break
                pre = stack.pop()
                ans[pre[1]] = numbers[i]
            stack.append((numbers[i], i))
        else:
            stack.append((numbers[i], i))

    for i in stack:
        ans[i[1]] = -1

    return ans
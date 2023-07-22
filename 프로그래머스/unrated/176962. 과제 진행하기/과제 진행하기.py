def solution(plans):
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(':'))
        plans[i][1] = (hour * 60) + minute
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1], reverse=True)
    ans, stack = [], []
    name, s, p = plans.pop()
    now = (name, s + p)
    time = s
    
    while plans:
        if now and time == now[1]:
            ans.append(now[0])
            now = tuple()
        if time == plans[-1][1]:
            if now: 
                stack.append((now[0], now[1] - time))
            name, s, p = plans.pop()
            now = (name, s + p)
        if not now and stack:
            name, s = stack.pop()
            now = (name, time + s)
        
        time += 1
    
    ans.append(now[0])
    while stack:
        ans.append(stack.pop()[0])
    
    return ans        
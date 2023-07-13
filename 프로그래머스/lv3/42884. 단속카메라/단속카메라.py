def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    ans = 0
    
    for i in range(len(routes)):
        if camera < routes[i][0]:
            ans += 1
            camera = routes[i][1]
    
    return ans
def solution(m, n, startX, startY, balls):
    ans = []
    
    for ball in balls:
        A = (ball[0], n + (n - ball[1]))
        B = (-ball[0], ball[1])
        C = (ball[0], -ball[1])
        D = (m + (m - ball[0]), ball[1])
        
        temp = int(1e9)
        for pos in (A, B, C, D):
            if startX == ball[0] and startY < ball[1] and pos == A:
                continue
            elif startY == ball[1] and startX > ball[0] and pos == B:
                continue
            elif startX == ball[0] and startY > ball[1] and pos == C:
                continue
            elif startY == ball[1] and startX < ball[0] and pos == D:
                continue
            
            distance = (abs(startX - pos[0]) ** 2) + ((abs(startY - pos[1])) ** 2)
            temp = min(temp, distance)
            
        ans.append(temp)
        
    return ans
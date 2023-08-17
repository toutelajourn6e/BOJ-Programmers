from collections import deque

def solution(n, t, m, timetable):
    timetable = deque(sorted(timetable, key=lambda x: (int(x[:2]), int(x[3:]))))
    cur = [9, 0]
    
    for i in range(n):
        capacity = m
        last = ''
        
        while capacity and timetable:
            hour, minute = int(timetable[0][:2]), int(timetable[0][3:])
            if hour < cur[0] or hour == cur[0] and minute <= cur[1]:
                last = timetable.popleft()
                capacity -= 1
            else: break
            
        if i == n-1:
            if capacity: return f"{str(cur[0]).zfill(2)}:{str(cur[1]).zfill(2)}"
            else:
                ans = [int(last[:2]), int(last[3:])]
                ans[1] -= 1
                if ans[1] < 0:
                    ans[0] -= 1
                    ans[1] = 59
                return f"{str(ans[0]).zfill(2)}:{str(ans[1]).zfill(2)}"
        
        cur[1] += t
        if cur[1] >= 60:
            cur[0] += 1
            cur[1] %= 60
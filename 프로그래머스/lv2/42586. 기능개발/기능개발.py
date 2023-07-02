from collections import deque

def solution(progresses, speeds):
    progresses, speeds = deque(progresses), deque(speeds)
    result, cnt = [], 0
    
    while progresses:
        for idx, speed in zip(range(len(progresses)), speeds):
            progresses[idx] += speed
        
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
        
        if cnt:
            result.append(cnt)
            cnt = 0
        
    return result
                
        
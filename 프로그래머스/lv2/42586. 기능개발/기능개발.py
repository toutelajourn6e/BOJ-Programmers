from collections import deque

def solution(progresses, speeds):
    progresses, speeds = deque(progresses), deque(speeds)
    result, temp = [], 0
    
    while progresses:
        for idx, speed in zip(range(len(progresses)), speeds):
            progresses[idx] += speed
        
        if progresses[0] >= 100:
            while True:
                if len(progresses) == 0 or progresses[0] < 100:
                    break
                progresses.popleft()
                speeds.popleft()
                temp += 1
                
            result.append(temp)
            temp = 0
        
    return result
                
        
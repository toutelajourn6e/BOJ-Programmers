from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    boat = 0
    temp = 0
    
    while True:
        if not len(people):
            break
            
        temp += people.pop()
        
        while True:
            if len(people) >= 1 and temp + people[0] <= limit:
                temp += people.popleft()
            else:
                boat += 1
                temp = 0
                break
    
    return boat
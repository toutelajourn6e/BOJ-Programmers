from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    ans = 0
    n = len(words)
    visit = [False] * n
    distance = [0] * (n + 1)
    
    q = deque()
    q.append(begin)
    
    while q:
        print(distance)
        word = q.popleft()
        
        for index, compare in enumerate(zip([word] * n, words)):
            if compare[0] == compare[1]:
                continue
            flag = False
            for b, w in zip(compare[0], compare[1]):
                if b != w:
                    if flag: break
                    else: flag = True
            else:
                if not visit[index]:
                    visit[index] = True
                    if word != begin:
                        distance[words.index(compare[1])] = distance[words.index(word)] + 1
                    else:
                        distance[words.index(compare[1])] = 1
                    q.append(compare[1])
    
    return distance[words.index(target)]
            
            
            
            
            
            
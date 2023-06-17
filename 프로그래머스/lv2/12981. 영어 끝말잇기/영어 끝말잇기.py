def solution(n, words):
    duplicate = {}
    for word in words:
        duplicate[word] = False
        
    pre = words[0][0]
    cnt = 0
    player = 0
    phase = 1

    while cnt < len(words):
        current = words[cnt]
        player += 1
        if player == n + 1:
            player = 1
        if cnt != 0 and cnt % n == 0:
            phase += 1

        if pre[-1] != current[0] or duplicate[current]:
            break
        
        cnt += 1
        duplicate[current] = True
        pre = current
        
    else:
        return [0, 0]
    
    return [player, phase]
def solution(survey, choices):
    character = {}
    
    for i in 'RTCFJMAN':
        character.setdefault(i, 0)
        
    board = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    
    for KBTI, choice in zip(survey, choices):
        if choice < 4:
            character[KBTI[0]] += board[choice]
        elif choice > 4:
            character[KBTI[1]] += board[choice]
            
            
    compare = ['RT', 'CF', 'JM', 'AN']
    result = ''
    
    for i in compare:
        if character[i[0]] > character[i[1]]:
            result += i[0]
        elif character[i[0]] < character[i[1]]:
            result += i[1]
        else:
            result += i[0]
            
    return result
    
    
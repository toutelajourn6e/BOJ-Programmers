def solution(record):
    nickname = {}
    result = []
    
    for i in record:
        info = i.split()
        if len(info) > 2:
            status, user_id, nick = info
            nickname[user_id] = nick
        
    for i in record:
        info = i.split()
        if info[0] == 'Enter':
            result.append(f"{nickname[info[1]]}님이 들어왔습니다.")
        elif info[0] == 'Leave':
            result.append(f"{nickname[info[1]]}님이 나갔습니다.")
    
    return result
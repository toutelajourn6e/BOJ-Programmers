def solution(s, skip, index): # z = 122
    new_s = []
    
    for i in s:
        cnt = 0
        temp = ord(i)
        while cnt < index:
            temp += 1
            if temp > ord('z'):
                temp = ord('a')
            if chr(temp) not in skip:
                cnt += 1
        new_s.append(chr(temp))
    
    return ''.join(new_s)
from string import ascii_uppercase

def solution(msg):
    ans = []
    dic = {}
    
    for idx, char in enumerate(ascii_uppercase):
        dic[char] = idx + 1
        
    cnt = 27
    idx = 0
    temp = ''
    while idx < len(msg):
        temp += msg[idx]
        if temp not in dic:
            dic[temp] = cnt
            cnt += 1
            ans.append(dic[temp[:-1]])
            temp = ''
        else: idx += 1
    
    if temp: ans.append(dic[temp])
    return ans
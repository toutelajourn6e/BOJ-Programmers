def solution(s):
    ans = []
    set_ans = set()
    s = s.split('},{')
    s[0] = s[0].replace('{', '')
    s[-1] = s[-1].replace('}', '')
    s.sort(key=lambda x: len(x))
    
    for i in range(len(s)):
        temp = s[i].split(',')
        for j in temp:
            if int(j) not in set_ans:
                ans.append(int(j))
                set_ans.add(int(j))
                
    return ans
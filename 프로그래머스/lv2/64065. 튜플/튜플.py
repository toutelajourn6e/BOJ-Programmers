def solution(s):
    ans = []
    set_ans = set()
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))

    for i in range(len(s)):
        temp = s[i].split(',')
        for j in temp:
            if int(j) not in set_ans:
                ans.append(int(j))
                set_ans.add(int(j))

    return ans
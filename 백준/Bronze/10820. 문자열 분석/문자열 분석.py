ans = [0]*4

while 1:
    try:
        s = input()
        for i in s:
            if i.islower():
                ans[0] += 1
            elif i.isupper():
                ans[1] += 1
            elif i.isdigit():
                ans[2] += 1
            elif i == ' ':
                ans[3] += 1
        print(*ans)
        ans = [0]*4
    except:
        break
 
    
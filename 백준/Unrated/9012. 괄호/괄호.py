import sys
t = int(input())

for _ in range(t):
    ps = input()
    vps_count = 0
    for i in ps:
        if i == "(":
            vps_count += 1
        else:
            vps_count -= 1
            if vps_count < 0:
                break
    if vps_count == 0:
        print('YES')
    else:
        print('NO')
    
            
            
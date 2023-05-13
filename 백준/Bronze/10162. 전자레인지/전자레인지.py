t = int(input())
buttons = [300, 60 ,10]
ans = []
for button in buttons:
    ans.append(t // button)
    t %= button
    
if t != 0:
    print(-1)
else:
    print(*ans)
n = int(input())
a = list(map(int, input().split()))
M = max(a)
new = list()

for i in a:
    i = (i/M)*100
    new.append(i)
    
print(sum(new)/len(new))
total = list(range(1, 31))

for i in range(28):
    a = int(input())
    
    if a in total:
        total.remove(a)
        
total.sort()
print(total[0])
print(total[1])
    
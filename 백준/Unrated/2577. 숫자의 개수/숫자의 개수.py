a = int(input())
b = int(input())
c = int(input())

m = str(a * b * c)
decimal = [0] * 10

for i in m:
    decimal[int(i)] += 1
    
for j in decimal:
    print(j)
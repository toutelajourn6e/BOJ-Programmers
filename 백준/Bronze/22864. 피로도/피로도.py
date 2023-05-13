a, b, c, m = map(int, input().split())
fatigue = 0
task = 0

for _ in range(24):
    if fatigue + a <= m:
        fatigue += a
        task += b
    else:
        fatigue -= c
        if fatigue < 0:
            fatigue = 0
    
print(task)
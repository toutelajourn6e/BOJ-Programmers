def hanoi(n, start=1, aux=2, end=3):
    if n == 1:
        print(f"{start} {end}")
        return
    
    hanoi(n-1, start, end, aux)
    
    print(f"{start} {end}")
    
    hanoi(n-1, aux, start, end)
    
n = int(input())
print((2 ** n)-1)
if n <= 20:
    hanoi(n)
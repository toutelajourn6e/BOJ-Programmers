n = int(input())
m = int(n**0.5)
result = n

for i in range(2, m+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        result *= 1 - (1 / i)
        
if n > 1:
    result *= 1 - (1 / n)
    
print(int(result))
    
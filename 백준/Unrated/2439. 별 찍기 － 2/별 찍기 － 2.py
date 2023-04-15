n = int(input())
output = ''

for j in reversed(range(n)):
    output += ' '*j
    output += '*'*(n-j)
    output += '\n'
    
print(output, end='')
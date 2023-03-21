bj_input = input()
answer = ''

for i in bj_input:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
        
print(answer)
        

s = input()
tag = False
stack = ''

for i in s:
    if i == '<':
        print(stack[::-1], end='')
        stack = ''
        tag = True
        stack += i
    elif i == '>':
        tag = False
        stack += i
        print(stack, end='')
        stack = ''
    elif tag == True:
        stack += i
    elif tag == False:
        if i == ' ':
            print(stack[::-1] + ' ',end ='')
            stack = ''
        else:
            stack += i
print(stack[::-1], end='')
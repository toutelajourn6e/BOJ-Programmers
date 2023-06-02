s = input()
s = s.replace('01', '0x1')
s = s.replace('10', '1x0')
s = list(s.split('x'))
one = 0
zero = 0
for i in s:
    if i[0] == '0':
        zero += 1
    else:
        one += 1
        
print(min(one, zero))
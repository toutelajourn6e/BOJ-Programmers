b = input()
unit = 3
dic = {
    '000': '0', '001':'1', '010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'
}
oc = ''

if len(b)%3 == 1:
    b = '00'+ b
elif len(b)%3 == 2:
    b = '0' + b
    
b = [b[i:i+unit] for i in range(0, len(b), unit)]

for i in b:
    oc += dic[i]

print(oc)
div = list()

for i in range(10):
    div.append(int(input())%42)
    
div = set(div)
print(len(div))

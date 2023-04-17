alpha = [0] * 26

for s in input(): 
    alpha[ord(s)-97]+=1
    
print(*alpha)

# A = 65, Z = 90, a = 97, z = 122 

def solution(s, n):
    ans = []
    
    for i in s:
        if i == ' ':
            ans.append(' ')
            continue
        
        if i.isupper():
            asc_code = ord(i)
            asc_code += n
            if asc_code > 90:
                asc_code = 64 + (asc_code % 90)
            ans.append(chr(asc_code))
            
        elif i.islower():
            asc_code = ord(i)
            asc_code += n
            if asc_code > 122:
                asc_code = 96 + (asc_code % 122)
            ans.append(chr(asc_code))
            
            
    return ''.join(ans)
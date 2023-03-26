def solution(my_string):
    my_string = my_string.lower()
    ascii_ls = list()
    answer = list()
    
    for s in my_string:
        ascii_ls.append(ord(s))
        
    ascii_ls.sort()
    
    for i in ascii_ls:
        answer.append(chr(i))
        
    return  ''.join(answer)

    
        
    
    
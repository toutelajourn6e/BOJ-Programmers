from string import ascii_lowercase

def solution(age):
    separate = ' '.join(str(age).split())
    answer = ''
    
    for i in separate:
        j = int(i)
        answer += ascii_lowercase[j]
        
    return answer

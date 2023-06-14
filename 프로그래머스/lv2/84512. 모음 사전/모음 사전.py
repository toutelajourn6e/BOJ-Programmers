dic = ['A', 'E', 'I', 'O', 'U']
result = 0

def product(word, temp):
    global result
    if word == temp:
        return True
    if len(temp) == 5:
        result += 1
        return False
    
    result += 1
    
    for i in range(5):
        temp += dic[i]
        if product(word, temp):
            return True
        else:
            temp = temp[:-1]
        

def solution(word):
    temp = ''
    product(word, temp)
    return result


def solution(numbers):
    result = []
    
    for num in numbers:
        if bin(num)[-1] == '0' or bin(num)[-2] == '0':
            result.append(num + 1)
        else:
            b_num = list(bin(num)[2:].zfill(len(bin(num))))
            for i in range(len(b_num)-1, -1, -1):
                if b_num[i] == '0':
                    b_num[i] = '1'
                    b_num[i+1] = '0'
                    break
            result.append(int(''.join(b_num), 2))   
            
    return result
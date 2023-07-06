def compare_distance(n, l, r, hand):
    l_distance = abs(l[0] - n[0]) + abs(l[1] - n[1])
    r_distance = abs(r[0] - n[0]) + abs(r[1] - n[1])
    if l_distance > r_distance:
        return 'R'
    elif l_distance < r_distance:
        return 'L'
    else:
        if hand == 'left':
            return 'L'
        else: return 'R'

def solution(numbers, hand):
    result = []
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2),}
    left_cur = '*'
    right_cur = '#'
    
    for num in numbers:
        if num in [1, 4, 7]:
            result.append('L')
            left_cur = num
        elif num in [3, 6, 9]:
            result.append('R')
            right_cur = num
        else: # 2, 5, 8, 0
            l = keypad[left_cur]
            r = keypad[right_cur]
            n = keypad[num]
            if compare_distance(n, l, r, hand) == 'L':
                result.append('L')
                left_cur = num
            else:
                result.append('R')
                right_cur = num
                
    return ''.join(result)
            
            
            
            
            
            
                
        
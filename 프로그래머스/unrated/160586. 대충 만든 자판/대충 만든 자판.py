from string import ascii_uppercase

def solution(keymap, targets):
    result = []
    key_dict = {}
    chars = ascii_uppercase
    
    for char in chars:
        min_idx = 100
        for k in keymap:
            if char in k:
                min_idx = min(min_idx, k.index(char))
        key_dict[char] = min_idx + 1
        
    for target in targets:
        press = 0
        for t in target:
            if key_dict[t] == 101:
                result.append(-1)
                break
            else:
                press += key_dict[t]
        else:
            result.append(press)
            
    return result
    
    
    
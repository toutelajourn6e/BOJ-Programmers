def solution(babbling):
    result = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:
        n = len(bab)
        for i in can:
            if i * 2  not in bab:
                bab = bab.replace(i, " " * len(i))
        if bab == " " * n:
            result += 1
            
    return result
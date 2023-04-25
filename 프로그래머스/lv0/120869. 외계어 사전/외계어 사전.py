def solution(spell, dic):
    ok = False
    
    for i in dic:
        for j in spell:
            if j in i:
                ok = True
                continue
            else:
                ok = False
                break
        if ok == True:
            return 1

    return 2
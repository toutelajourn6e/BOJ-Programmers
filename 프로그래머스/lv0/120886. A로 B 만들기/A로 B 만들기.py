def solution(before, after):
    after = list(after)
    for i in before:
        try:
            after.remove(i)
        except:
            pass
        
    if len(after) == 0: return 1
    else: return 0
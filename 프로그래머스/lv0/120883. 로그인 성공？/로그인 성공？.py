def solution(id_pw, db):
    ans = ''
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            return 'login'
        elif id_pw[0] == i[0]:
            ans = 'wrong pw'
    
    if ans == 'wrong pw':
        return ans
    else:
        return 'fail'
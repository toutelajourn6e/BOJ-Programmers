def check(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    return False if stack else True

def separate(w):
        u, v = '', ''
        l_cnt = r_cnt = 0
        
        for i in range(len(w)):
            if w[i] == '(': l_cnt += 1
            else: r_cnt += 1
            u += w[i]
            if l_cnt == r_cnt:
                v = w[i+1:]
                break
        
        if check(u):
            if v: u += separate(v)
        else:
            temp = '('
            temp += separate(v)
            temp += ')'
            u = u[1:-1]
            u = list(u)
            for i in range(len(u)):
                if u[i] == '(': u[i] = ')'
                else: u[i] = '('
            u = temp + ''.join(u)
        return u
                
def solution(p):
    if p == '':
        return ''
    return separate(p)
    
    
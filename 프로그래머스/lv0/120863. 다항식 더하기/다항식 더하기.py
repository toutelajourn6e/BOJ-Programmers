def solution(polynomial):
    monomial = polynomial.split(' + ')
    x = 0
    c = 0
    for i in monomial:
        if i[-1] == 'x':
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
        elif i == '0':
            continue
        else:
            c += int(i)
            
    if x == 0:
        return str(c)
    elif c == 0:
        if x == 1:
            return 'x'
        return str(x) + 'x'
    else:
        if x == 1:
            return 'x' + ' + ' + str(c)
        return (str(x) + 'x') + ' + ' + str(c)
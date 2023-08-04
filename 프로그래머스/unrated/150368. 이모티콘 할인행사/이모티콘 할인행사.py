from itertools import product

def solution(users, emoticons):
    result = [0, 0]
    n = len(emoticons)
    prod = list(product([10, 20, 30, 40], repeat=n))
    
    for p in prod:
        plus, sale = 0, 0
        for want_dis, upper in users:
            total = 0
            for emoticon, discount in zip(emoticons, p):
                if discount >= want_dis:
                    total += emoticon - int(emoticon * (discount / 100))
            if total >= upper: plus += 1
            else: sale += total
            
        if plus > result[0]:
            result[0] = plus
            result[1] = sale
        elif plus == result[0] and sale > result[1]:
            result[1] = sale
    
    return result
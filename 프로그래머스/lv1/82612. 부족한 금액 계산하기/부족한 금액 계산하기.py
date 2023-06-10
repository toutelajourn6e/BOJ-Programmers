def solution(price, money, count):
    pay = sum([price * i for i in range(1, count+1)])
    return pay - money if pay > money else 0
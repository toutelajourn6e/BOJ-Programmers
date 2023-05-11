def solution(chicken):
    coupon = chicken
    service = 0
    while 1:
        temp = 0
        if coupon // 10 == 0:
            break
        service += coupon // 10
        temp += coupon // 10
        coupon %= 10
        coupon += temp
        
    return service
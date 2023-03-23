def solution(price):
    if price >= 500000:
        return int(price - ((price / 100) * 20))
    elif price >= 300000:
        return int(price - ((price / 100) * 10))
    elif price >= 100000:
        return int(price - ((price / 100) * 5))
    else:
        return price
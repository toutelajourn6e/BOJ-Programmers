def solution(storey):
    ans = 0
    
    while storey:
        storey, press = divmod(storey, 10)
        if press > 5 or (press == 5 and storey % 10 >= 5):
            press = 10 - press
            storey += 1
        ans += press
    return ans
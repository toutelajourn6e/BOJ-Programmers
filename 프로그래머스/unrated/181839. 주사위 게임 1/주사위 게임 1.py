def solution(a, b):
    mod_a = a % 2; mod_b = b % 2;
    if mod_a and mod_b:
        return (a ** 2) + (b ** 2)
    elif not mod_a and not mod_b:
        return abs(a - b)
    else:
        return 2 * (a + b)
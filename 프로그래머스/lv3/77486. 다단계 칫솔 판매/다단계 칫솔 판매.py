from collections import defaultdict

def solution(enroll, referral, seller, amount):
    ans = [0] * len(enroll)
    profit = defaultdict(int)
    relations = defaultdict(str)
    info = defaultdict(int)
    
    for salesman, cnt in zip(seller, amount):
        profit[salesman] += 100 * cnt
        
    for idx, relation in enumerate(zip(enroll, referral)):
        salesman, boss = relation
        relations[salesman] = boss
        info[salesman] = idx
        
    def distribute(person, rest):
        commission = int(rest / 10)
        if commission < 1:
            ans[info[person]] += rest
            return
        take = rest - commission
        ans[info[person]] += take
        if relations[person] == '-':
            return
        distribute(relations[person], commission)
    
    for salesman, cnt in zip(seller, amount):
        distribute(salesman, cnt * 100)
    
    return ans
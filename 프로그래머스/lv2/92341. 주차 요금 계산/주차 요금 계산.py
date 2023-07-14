from collections import defaultdict

def solution(fees, records):
    dft_time, dft_fee, unit_time, unit_fee = fees
    time_cnt = defaultdict(int)
    inout = defaultdict(int)
    total_fee = defaultdict(int)
    
    for record in records:
        time, car_num, act = record.split()
        hour, minute = map(int, time.split(':'))
        if act == 'IN':
            inout[car_num] = (hour * 60) + minute
        else:
            time_cnt[car_num] += ((hour * 60) + minute) - inout[car_num]
            inout[car_num] = None
    
    for left_car in inout:
        if inout[left_car] != None:
            time_cnt[left_car] += ((23 * 60) + 59) - inout[left_car]
    
    for car_num in time_cnt:
        time_cnt[car_num] -= dft_time
        total_fee[car_num] += dft_fee
        if time_cnt[car_num] <= 0: continue
        div, mod = divmod(time_cnt[car_num], unit_time)
        total_fee[car_num] += div * unit_fee
        if mod: total_fee[car_num] += unit_fee
    
    
    result = [0] * len(total_fee)
    
    for idx, car_num in zip(range(len(result)), sorted(total_fee)):
        result[idx] = total_fee[car_num]
        
    return result
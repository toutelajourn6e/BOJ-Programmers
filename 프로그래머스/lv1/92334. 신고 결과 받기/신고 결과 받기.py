from collections import defaultdict

def solution(id_list, report, k):
    report_cnt = defaultdict(set)
    
    for content in report:
        send, receive = content.split()
        report_cnt[receive].add(send)
        
    notice = defaultdict(int)
    for user in report_cnt:
        if len(report_cnt[user]) >= k:
            for i in report_cnt[user]:        
                notice[i] += 1
                
    for i in range(len(id_list)):
        id_list[i] = notice[id_list[i]]
        
    return id_list
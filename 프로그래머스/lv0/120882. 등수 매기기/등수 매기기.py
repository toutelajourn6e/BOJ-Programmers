def solution(score):
    ans = []
    avg = []
    
    for i,j in score: # 평균 구하기
        avg.append((i+j)/2)
        
    sort_avg = sorted(avg, reverse=True)
    
    
    for i in avg:
        ans.append(sort_avg.index(i)+1)
        
    return ans
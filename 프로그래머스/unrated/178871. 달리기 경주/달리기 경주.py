def solution(players, callings):
    grade = {i : players for i, players in enumerate(players)}
    grade_rev = {players : i for i, players in enumerate(players)}

    for j in callings:
        call_num = grade_rev[j] # 호명 선수 등수
        call_name = grade[call_num] # 호명 선수 이름
        
        other_name = grade[call_num-1] # 앞 선수 이름
        other_num = grade_rev[other_name] # 앞 선수 번호
        
        # 앞 선수와 호명 선수 (이름, 등수) 교환
        grade_rev[call_name], grade_rev[other_name] = grade_rev[other_name], grade_rev[call_name]
        grade[call_num], grade[other_num] = grade[other_num], grade[call_num]
        
    return list(grade.values())
        
        
        
        
       
        
    

        
        

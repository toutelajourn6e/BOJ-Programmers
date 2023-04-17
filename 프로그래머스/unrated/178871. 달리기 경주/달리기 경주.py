def solution(players, callings):
    grade = {i : players for i, players in enumerate(players)}
    grade_rev = {players : i for i, players in enumerate(players)}

    for j in callings:
        call_num = grade_rev[j]
        call_name = grade[call_num]
        
        other_name = grade[call_num-1]
        other_num = grade_rev[other_name]
        
        grade_rev[call_name], grade_rev[other_name] = grade_rev[other_name], grade_rev[call_name]
        grade[call_num], grade[other_num] = grade[other_num], grade[call_num]
        
    return list(grade.values())
        
        
        
        
       
        
    

        
        

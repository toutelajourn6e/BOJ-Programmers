def solution(skill, skill_trees):
    result = 0
    skill_set = set(skill)
    
    for skill_tree in skill_trees:
        idx = 0
        for i in skill_tree:
            if i in skill_set:
                if i == skill[idx]:
                    idx += 1
                else:
                    break
        else:
            result += 1
            
    return result
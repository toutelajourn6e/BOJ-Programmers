from itertools import permutations
import re

def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*', '.')
    ans = set()
    
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            ans.add(''.join(sorted(i)))
            
    return len(ans)
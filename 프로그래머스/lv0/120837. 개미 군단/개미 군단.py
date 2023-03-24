def solution(hp):
    ant = {
        'demage5': '',
        'demage3': '',
        'demage1': ''
    }
    
    ant['demage5'] = hp // 5
    ant['demage3'] = (hp % 5) // 3
    ant['demage1'] = ((hp % 5) % 3) 
    
    return sum(ant.values())
    
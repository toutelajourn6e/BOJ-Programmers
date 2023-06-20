import datetime

def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    
    today = days[datetime.date(2016, a, b).weekday()]
    
    return today
    
def solution(today, terms, privacies):
    year, month, day = map(int, today.split('.'))
    expiry = {}
    result = []
    
    for term in terms:
        typ, span = term.split()
        expiry[typ] = int(span)
        
    for index, privacy in enumerate(privacies):
        date, typ = privacy.split()
        ex_year, ex_month, ex_day = map(int, date.split('.'))
        ex_month = ex_month + expiry[typ]
        if ex_month % 12 != 0:
            exceed, ex_month = divmod(ex_month, 12)
            ex_year = ex_year + exceed
        else:
            exceed = (ex_month // 12) - 1
            ex_month = 12
            ex_year = ex_year + exceed
    
        if ex_year == year and ex_month == month and ex_day == day:
            result.append(index+1)
            continue
        elif ex_year > year:
            continue
        elif ex_year == year and ex_month > month:
            continue
        elif ex_year == year and ex_month == month and ex_day > day:
            continue
            
        result.append(index+1)
        
            
        
    return result
            
        
    
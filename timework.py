import datetime as dt

def get_weekday(tomorrow=False) -> int:
    weekday = dt.datetime.isoweekday(dt.datetime.today())
    if tomorrow:
        if weekday == 7:
            return 1
        
        return weekday
    else:
        return weekday
            
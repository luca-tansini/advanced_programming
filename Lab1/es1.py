import calendar

def findNextLeap(year):
    return (calendar.isleap(year) and year) or findNextLeap(year+1);

def howManyLeapYears(y1,y2):
    cont=0
    for i in range(y1,y2):
        if calendar.isleap(i):
            cont+=1
    return cont

def whichDayOfTheWeek(day,month,year):
    calendar.setfirstweekday(0)
    return list(calendar.day_name)[calendar.weekday(year,month,day)]

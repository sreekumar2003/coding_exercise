import calendar

mon,day,year = map(int,input().split())
daynr = calendar.weekday(year,mon,day)
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[daynr])

'''
input
08 05 2015 MM DD YYYY

ouput

MONDAY

import datetime

def solution(a, b):
    answer = ''
    count = (datetime.date(2016, a, b) - datetime.date(2016, 1, 1)).days
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = day[count%7]
    return answer

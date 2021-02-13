# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return weekdays[(sum(days_of_month[:a]) + b + 4) % 7]
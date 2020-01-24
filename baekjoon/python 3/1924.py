# 문제 링크: https://www.acmicpc.net/problem/1924

m, d = map(int, input().split())

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total_day = sum(month_days[:m]) + d

print(day_of_week[total_day % 7])

# 문제 링크: https://level.goorm.io/exam/43137/%EC%9A%94%EC%9D%BC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

m, d = map(int, input().split())

days = ['MON', 'THU', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if d <= month_days[m]:
    print(days[(3 + sum(month_days[:m]) + d) % 7])
else:
    print('ERROR')
# 문제 링크: https://level.goorm.io/exam/43204/%EC%9C%A4%EB%85%84-leap-year/quiz/1

y = int(input())

print('Leap Year' if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 'Not Leap Year')

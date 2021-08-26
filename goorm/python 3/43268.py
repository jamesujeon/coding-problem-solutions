# 문제 링크: https://level.goorm.io/exam/43268/%EC%A0%84%EA%B8%B0%EC%9A%94%EA%B8%88/quiz/1

value = int(input())


tax = 1
if value < 100:
    tax = .5
elif value < 200:
    tax = .7
elif value < 300:
    tax = .9

print('{:.2f}'.format(value * tax * 0.01))
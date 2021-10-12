# 문제 링크: https://level.goorm.io/exam/43143/삼각형의-넓이-2/quiz/1

a, b, c = map(int, input().split())


s = (a + b + c) / 2
S = (s * (s - a) * (s - b) * (s - c))**.5


print('{:.2f}'.format(S))
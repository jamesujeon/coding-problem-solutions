# 문제 링크: https://level.goorm.io/exam/43068/1a-%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5-%EC%B2%AD%EC%86%8C%EA%B8%B0/quiz/1

inputs = [map(int, input().split()) for _ in range(int(input()))]

for X, Y, N in inputs:
	diff = N - (abs(X) + abs(Y))
	print('YES' if diff >= 0 and diff % 2 == 0 else 'NO')
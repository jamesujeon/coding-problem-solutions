# 문제 링크: https://level.goorm.io/exam/43196/%EC%84%B8%EB%A1%9C-%EC%88%9C%EC%84%9C-%EC%82%AC%EA%B0%81%ED%98%95/quiz/1

n = int(input())

for i in range(1, n + 1):
	for j in range(n):
		print(i + j * n, end=' ')
	print()
# 문제 링크: https://level.goorm.io/exam/43209/%EC%95%94%EC%8A%A4%ED%8A%B8%EB%A1%B1-%EC%88%98-narcissistic-number/quiz/1

a, b = map(int, input().split())

for i in range(a, b + 1):
	if sum(int(d)**3 for d in str(i)) == i:
		print(i, end=' ')
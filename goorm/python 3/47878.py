# 문제 링크: https://level.goorm.io/exam/47878/%EC%82%AC%EC%9D%80%ED%92%88-%EA%B5%90%ED%99%98%ED%95%98%EA%B8%B0/quiz/1

counts = []
for _ in range(int(input())):
	N, M = map(int, input().split())

	counts.append(min(N // 5, (N + M) // 12))


for count in counts:
	print(count)

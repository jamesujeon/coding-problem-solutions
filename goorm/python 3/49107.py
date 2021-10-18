# 문제 링크: https://level.goorm.io/exam/49107/%EC%86%8C%ED%9D%AC%EC%99%80-%EB%B2%84%EC%8A%A4/quiz/1

N, T = map(int, input().split())
times = [map(int, input().split()) for _ in range(N)]


for i, (s, d) in enumerate(times):
	while s < T:
		s += d
	times[i] = s - T

min_time = min(times)
for i, time in enumerate(times):
	if time == min_time:
		print(i + 1)
		break
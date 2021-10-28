# 문제 링크: https://level.goorm.io/exam/48134/%EB%B0%A9-%EB%B0%B0%EC%A0%95-%EC%B4%88%EB%93%B1%EB%B6%80/quiz/1

from math import ceil

N, K = map(int, input().split())
students = [map(int, input().split()) for _ in range(N)]


counts = [[0] * 6 for _ in range(2)]
for S, Y in students:
	counts[S][Y - 1] += 1

room_count = sum(
	sum(map(lambda x: ceil(x / K), counts))
	for counts in counts
)


print(room_count)
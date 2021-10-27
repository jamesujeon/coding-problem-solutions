# 문제 링크: https://level.goorm.io/exam/43059/%ED%8C%8C%EB%8F%84-%EC%84%BC%EC%84%9C/quiz/1

X, Y, R = map(int, input().split())
points = list(list(map(int, input().split())) for _ in range(5))


result = -1
for i in range(len(points)):
	distance = ((points[i][0] - X)**2 + (points[i][1] - Y)**2)**.5
	if distance <= R:
		R = distance
		result = i + 1


print(result)
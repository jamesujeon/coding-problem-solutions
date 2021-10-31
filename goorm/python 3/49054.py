# 문제 링크: https://level.goorm.io/exam/49054/%EC%96%B4%EB%A0%A4%EC%9A%B4-%EB%AC%B8%EC%A0%9C/quiz/1

N = int(input())


result = 1
for i in range(1, N + 1):
	result *= i

while result > 9:
	result = sum(map(int, str(result)))


print(result)
# 문제 링크: https://level.goorm.io/exam/43202/%EB%8B%A4%EC%9D%B4%EC%95%84%EB%AA%AC%EB%93%9C/quiz/1

n = int(input())


half = n // 2

for i in range(1, half + 1):
	print(' ' * (half - i + 1) + '*' * (i * 2 - 1))

if n % 2:
	print('*' * n)

for i in range(1, half + 1):
	print(' ' * i + '*' * ((half - i + 1) * 2 - 1))
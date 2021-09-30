# 문제 링크: https://level.goorm.io/exam/43096/%EC%86%8C%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

N = int(input())


primes = [0] * 2 + [1] * (N - 1)
for i in range(2, N + 1):
	if primes[i]:
		for j in range(i**2, N + 1, i):
			primes[j] = 0


print(primes.count(1))

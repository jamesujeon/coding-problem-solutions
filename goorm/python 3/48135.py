# 문제 링크: https://level.goorm.io/exam/48135/%ED%83%80%EC%9D%BC-%EC%9E%A5%EC%8B%9D%EB%AC%BC/quiz/1

N = int(input())


dp = [0, 1, 1, 2, 3]
for i in range(5, max(N, 4) + 1):
	dp.append(dp[i - 1] + dp[i - 3] + dp[i - 4])


print((dp[N] * 2 + dp[N - 1]) * 2)
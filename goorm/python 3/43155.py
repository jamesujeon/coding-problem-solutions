# 문제 링크: https://level.goorm.io/exam/43155/%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-binomial-coefficient/quiz/1

n, k = map(int, input().split())

dp = {}
for i in range(n + 1):
    dp[(i, 0)] = 1
for i in range(k + 1):
    dp[(0, i)] = 0
    dp[(i, i)] = 1

if (n, k) not in dp:
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[(i, j)] = dp[(i - 1, j - 1)] + dp[(i - 1, j)]

print(dp[(n, k)])
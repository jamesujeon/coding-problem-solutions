# 문제 링크: https://level.goorm.io/exam/43264/n-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

N = int(input())


n = 1
while (n * (n + 1)) // 2 < N:
    n += 1


print(n)
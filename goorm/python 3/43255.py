# 문제 링크: https://level.goorm.io/exam/43255/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
# 문제 링크: https://level.goorm.io/exam/43168/%EC%95%94%ED%98%B8%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

a, b, n = map(int, input().split())

print(sum(n ** i for i in range(a, b + 1)))
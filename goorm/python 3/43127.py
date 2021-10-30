# 문제 링크: https://level.goorm.io/exam/43127/%ED%99%80%EC%88%98-%EB%86%80%EC%9D%B4/quiz/1

n = int(input())

print((sum(i * 2 - 1 for i in range(1, n + 1)) * 2 - 3) * 3)
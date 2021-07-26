# 문제 링크: https://level.goorm.io/exam/43116/%EC%99%84%EC%A0%84-%EC%A0%9C%EA%B3%B1%EC%88%98/quiz/1

from math import ceil, floor

m, n = map(int, input().split())

squares = [i * i for i in range(ceil(m**.5), floor(n**.5) + 1)]

print(min(squares), sum(squares))
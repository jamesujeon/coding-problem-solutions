# 문제 링크: https://level.goorm.io/exam/47881/%EA%B7%BC%EB%AC%B5%EC%9E%90%ED%9D%91/quiz/1

from math import ceil

N, K = map(int, input().split())
nums = list(map(int, input().split()))


print(ceil((N - K) / (K - 1)) + 1)

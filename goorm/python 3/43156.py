# 문제 링크: https://level.goorm.io/exam/43156/피자-쿠폰/quiz/1

n, m = map(int, input().split())


total = n
while n >= m:
    total += n // m
    n = n % m + n // m


print(total)
# 문제 링크: https://level.goorm.io/exam/49113/%EC%B5%9C%EB%8C%80-%EC%9E%90%EB%A6%AC%EA%B3%B1/quiz/1

from math import prod

n = input()


result = prod(map(int, n))
for i in range(len(n) - 1):
    if i > 0 and int(n[i]) <= 1:
        break

    result = max(prod(map(int, n[:i])) * max(int(n[i]) - 1, 1) * (9 ** (len(n) - i - 1)), result)


print(result)
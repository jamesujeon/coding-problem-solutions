# 문제 링크: https://level.goorm.io/exam/49098/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/quiz/1

import math

N = int(input())


count = 0
for i in range(1, int(math.log(N, 5)) + 1):
    count += N // (5**i)


print(count)

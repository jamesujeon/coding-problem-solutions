# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68645

from itertools import chain

def solution(n):
    nums = [[0] * (i + 1) for i in range(n)]
    i, j, num = -1, 0, 1
    for step in range(n):
        for _ in range(step, n):
            if step % 3 == 0:
                i += 1
            elif step % 3 == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            nums[i][j] = num
            num += 1
    return list(chain(*nums))
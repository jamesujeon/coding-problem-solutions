# 문제 링크: https://level.goorm.io/exam/48193/막대기/quiz/1

import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]


min_height = count = 0
for height in reversed(heights):
    if height > min_height:
        min_height = height
        count += 1


print(count)
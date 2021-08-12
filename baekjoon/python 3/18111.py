# 문제 링크: https://www.acmicpc.net/problem/18111

from collections import Counter
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = Counter(h for _ in range(N) for h in map(int, input().split()))


def get_time(base, blocks):
    time = 0
    for height, count in heights.items():
        diff = abs(height - base) * count
        if height > base:
            time += diff * 2
            blocks += diff
        else:
            time += diff
            blocks -= diff

    return time if blocks >= 0 else sys.maxsize


min_time, max_height = sys.maxsize, 0
for height in range(min(heights), max(heights) + 1):
    time = get_time(height, B)
    if time <= min_time:
        min_time = time
        max_height = height


print(min_time, max_height)
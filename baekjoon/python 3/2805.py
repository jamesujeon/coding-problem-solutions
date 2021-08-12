# 문제 링크: https://www.acmicpc.net/problem/2805

from collections import Counter

N, M = map(int, input().split())
heights = Counter(map(int, input().split()))


def sum_heights(base):
    return sum((h - base) * c for h, c in heights.items() if h > base)

max_height = 0
low, high = 0, max(heights)
while low <= high:
    mid = (low + high) // 2
    if sum_heights(mid) >= M:
        max_height = mid
        low = mid + 1
    else:
        high = mid - 1


print(max_height)
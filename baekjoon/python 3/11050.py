# 문제 링크: https://www.acmicpc.net/problem/11050

from functools import lru_cache

n, k = map(int, input().split())

@lru_cache()
def bino(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    return bino(n - 1, k) + bino(n - 1, k - 1)

print(bino(n, k))
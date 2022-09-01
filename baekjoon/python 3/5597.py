# 문제 링크: https://www.acmicpc.net/problem/5597

import sys
input = sys.stdin.readline

result = set(range(1, 31)) - set(int(input()) for _ in range(28))

print(min(result))
print(max(result))

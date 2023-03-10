# 문제 링크: https://www.acmicpc.net/problem/17350

import sys
input = sys.stdin.readline

print(f"뭐야{'?;'['anj' in (input().rstrip() for _ in range(int(input())))]}")

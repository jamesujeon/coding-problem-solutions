# 문제 링크: https://www.acmicpc.net/problem/4141

import sys
input = sys.stdin.readline

nums = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
nums = {c: k for k, v in nums.items() for c in v}

for _ in range(int(input())):
    n = [nums[c] for c in input().strip().upper()]
    print('YES' if n == n[::-1] else 'NO')

# 문제 링크: https://www.acmicpc.net/problem/2156

import sys

input()
amounts = map(int, sys.stdin)

max_amounts = (0, 0, 0)
for amount in amounts:
  max_amounts = (
    max(max_amounts),
    max_amounts[0] + amount,
    max_amounts[1] + amount
  )

print(max(max_amounts))
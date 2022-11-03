# 문제 링크: https://www.acmicpc.net/problem/6784

import sys
input = sys.stdin.readline

N = int(input())
responses = [input() for _ in range(N)]
answers = [input() for _ in range(N)]

print(sum(r == a for r, a in zip(responses, answers)))

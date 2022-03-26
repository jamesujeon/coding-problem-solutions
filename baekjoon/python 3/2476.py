# 문제 링크: https://www.acmicpc.net/problem/2476

import sys
input = sys.stdin.readline

def get_reward(input):
    a, b, c = sorted(map(int, input.split()))
    if a == b and b == c:
        return 10000 + a * 1000
    elif a == b or b == c:
        return 1000 + b * 100
    else:
        return max(a, b, c) * 100

print(max(get_reward(input()) for _ in range(int(input()))))

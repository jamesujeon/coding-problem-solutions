# 문제 링크: https://www.acmicpc.net/problem/4998

from math import ceil, log
import sys
input = sys.stdin.readline

while True:
    try:
        N, B, M = map(float, input().split())
        print(ceil(log(M / N, 1 + B / 100)))

    except:
        break

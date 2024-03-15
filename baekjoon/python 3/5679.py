# 문제 링크: https://www.acmicpc.net/problem/5679

import sys
input = sys.stdin.readline

while (H := int(input())) != 0:
    S = [H]
    while S[-1] > 1:
        S.append(S[-1] * 3 + 1 if S[-1] % 2 else S[-1] // 2)

    print(max(S))

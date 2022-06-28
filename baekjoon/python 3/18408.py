# 문제 링크: https://www.acmicpc.net/problem/18408

A, B, C = map(int, input().split())

if A == B or B == C:
    print(B)
else:
    print(C)

# counts = {1: 0, 2: 0}
# for i in [A, B, C]:
#     counts[i] += 1

# print(1 if counts[1] > counts[2] else 2)

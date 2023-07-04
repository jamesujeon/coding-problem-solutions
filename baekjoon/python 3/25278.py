# 문제 링크: https://www.acmicpc.net/problem/25278

import sys
input = sys.stdin.readline

changes = {"ox": 0, "oc": 0, "te": -30}
for _ in range(int(input())):
    c, v = input().split()
    changes[c[:2]] += int(v)

if changes["ox"] > 13 and changes["oc"] > 8 and changes["te"] > 7:
    print("liveable")
else:
    print("not liveable")

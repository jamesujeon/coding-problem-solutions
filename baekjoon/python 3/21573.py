# 문제 링크: https://www.acmicpc.net/problem/21573

tr, tc = map(int, input().split())
mode = input()

if mode == "freeze":
    tr = min(tr, tc)
elif mode == "heat":
    tr = max(tr, tc)
elif mode == "auto":
    tr = tc

print(tr)

# 문제 링크: https://www.acmicpc.net/problem/16431

Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

Bt = max(abs(Br - Jr), abs(Bc - Jc))
Dt = abs(Dr - Jr) + abs(Dc - Jc)

if Bt < Dt:
    print("bessie")
elif Bt > Dt:
    print("daisy")
else:
    print("tie")

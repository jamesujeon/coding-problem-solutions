# 문제 링크: https://www.acmicpc.net/problem/22938

X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

print("YES" if (X1 - X2)**2 + (Y1 - Y2)**2 < (R1 + R2)**2 else "NO")

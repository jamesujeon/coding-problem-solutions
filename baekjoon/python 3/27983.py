# 문제 링크: https://www.acmicpc.net/problem/27983

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = input().split()

def process(i, a, b, c):
    if X[i] - L[i] <= b[0]:
        return None, (b[1], i + 1)
    elif X[i] - L[i] <= c[0]:
        return None, (c[1], i + 1)
    if X[i] + L[i] > a[0]:
        return (X[i] + L[i], i + 1), None
    return a, None

result = ()
R = Y = B = (-10**10, 0)
for i in range(N):
    if C[i] == 'R':
        R, result = process(i, R, Y, B)
    elif C[i] == 'Y':
        Y, result = process(i, Y, R, B)
    else:
        B, result = process(i, B, R, Y)
    if result:
        break

if result:
    print("YES")
    print(*result)
else:
    print("NO")

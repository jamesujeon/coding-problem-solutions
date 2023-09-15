# 문제 링크: https://www.acmicpc.net/problem/26906

T = {}
for _ in range(int(input())):
    x, y = input().split()
    T[y] = x

N = input()
print(''.join(T.get(N[i:i + 4], '?') for i in range(0, len(N), 4)))

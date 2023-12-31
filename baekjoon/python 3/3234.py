# 문제 링크: https://www.acmicpc.net/problem/3234

X, Y = map(int, input().split())
K, R = int(input()), input()

t = []
p = [0, 0]
for i in range(K + 1):
    if abs(p[0] - X) < 2 and abs(p[1] - Y) < 2:
        t.append(i)
    if i < K:
        if R[i] == 'I':
            p[0] += 1
        elif R[i] == 'S':
            p[1] += 1
        elif R[i] == 'Z':
            p[0] -= 1
        elif R[i] == 'J':
            p[1] -= 1

print('\n'.join(map(str, t)) if t else -1)

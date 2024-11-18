# 문제 링크: https://www.acmicpc.net/problem/14686

n = int(input())
t1, t2 = list(map(int, input().split())), list(map(int, input().split()))

r, d = [0, 0], 0
for i in range(n):
    r[0] += t1[i]
    r[1] += t2[i]
    if r[0] == r[1]:
        d = i + 1

print(d)

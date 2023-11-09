# 문제 링크: https://www.acmicpc.net/problem/1681

N, L = input().split()

i = 0
for _ in range(int(N)):
    i += 1
    while L in str(i):
        i += 1

print(i)

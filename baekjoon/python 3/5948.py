# 문제 링크: https://www.acmicpc.net/problem/5948

N = int(input())

r = set()
while N not in r:
    r.add(N)
    N = int(str(N).zfill(4)[1:3])**2

print(len(r))

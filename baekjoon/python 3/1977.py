# 문제 링크: https://www.acmicpc.net/problem/1977

n = [i for i in range(int(input()), int(input()) + 1) if int(i**.5)**2 == i]

if n:
    print(sum(n))
    print(n[0])
else:
    print(-1)

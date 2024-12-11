# 문제 링크: https://www.acmicpc.net/problem/15155

n, k = map(int, input().split())
a = list(map(int, input().split()))

b = [0]
for i in a:
    if b[-1] + i > k:
        b.append(0)
    b[-1] += i

print(len(b))

# 문제 링크: https://www.acmicpc.net/problem/15234

n, k = map(int, input().split())
s = sorted(map(int, input().split()))

p = set()
l, r = 0, n - 1
while l < r:
    if s[l] + s[r] == k:
        p.add((s[l], s[r]))
        l += 1
        r -= 1
    elif s[l] + s[r] < k:
        l += 1
    else:
        r -= 1

print(len(p))

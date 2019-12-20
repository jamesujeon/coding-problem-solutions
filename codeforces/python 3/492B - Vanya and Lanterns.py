# 문제 링크: http://codeforces.com/problemset/problem/492/B

_, l = map(int, input().split())

a = sorted(list(map(int, input().split())))

d = max(a[i + 1] - a[i] for i in range(len(a) - 1)) / 2 if len(a) > 1 else l / 2
d = max(d, a[0], l - a[-1])

print(d)
# 문제 링크: http://codeforces.com/problemset/problem/339/B

n, _ = map(int, input().split())
a = list(map(int, input().split()))

result = sum(n for i in range(len(a) - 1) if a[i] > a[i + 1]) + a[-1] - 1

print(result)
# 문제 링크: http://codeforces.com/problemset/problem/160/A

n = int(input())
values = sorted(map(int, input().split()))

total = 0
while (total <= sum(values)):
  total += values.pop()

print(n - len(values))
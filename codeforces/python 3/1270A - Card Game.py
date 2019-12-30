# 문제 링크: https://codeforces.com/contest/1270/problem/A

max_cases = [(input(), max(map(int, input().split())), max(map(int, input().split())))[1:] for _ in range(int(input()))]

for max_f, max_s in max_cases:
  print('YES' if max_f > max_s else 'NO')
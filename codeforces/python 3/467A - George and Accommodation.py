# 문제 링크: http://codeforces.com/problemset/problem/467/A

pq = [tuple(map(int, input().split())) for _ in range(int(input()))]

result = sum(1 if q - p >= 2 else 0 for p, q in pq)

print(result)
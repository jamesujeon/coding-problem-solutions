# 문제 링크: http://codeforces.com/problemset/problem/148/A

*a, d = [int(input()) for _ in range(5)]

result = sum(any(map(lambda x: i % x == 0, a)) for i in range(1, d + 1))

print(result)
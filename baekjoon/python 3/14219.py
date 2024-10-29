# 문제 링크: https://www.acmicpc.net/problem/14219

n, m = sorted(map(int, input().split()))
print(['YES', 'NO'][(n * m) % 3 > 0])

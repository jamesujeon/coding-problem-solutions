# 문제 링크: http://codeforces.com/problemset/problem/69/A

vectors = [tuple(map(int, input().split())) for _ in range(int(input()))]

print('YES' if not any(map(sum, zip(*vectors))) else 'NO')
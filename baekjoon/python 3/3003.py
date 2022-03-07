# 문제 링크: https://www.acmicpc.net/problem/3003

pieces = list(map(int, input().split()))

pieces = [count - pieces[i] for i, count in enumerate([1, 1, 2, 2, 2, 8])]

print(' '.join(map(str, pieces)))

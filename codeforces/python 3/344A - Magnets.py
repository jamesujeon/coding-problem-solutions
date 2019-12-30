# 문제 링크: https://codeforces.com/problemset/problem/344/A

magnets = list(int(input()) for _ in range(int(input())))

count = 1 + sum(magnets[i] - magnets[i + 1] != 0 for i in range(len(magnets) - 1))

print(count)
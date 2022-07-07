# 문제 링크: https://www.acmicpc.net/problem/3578

h = int(input())

print('4' * (h % 2) + '8' * (h // 2) if h > 1 else '10'[h])

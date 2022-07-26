# 문제 링크: https://www.acmicpc.net/problem/21633

k = int(input())

print(f'{min(max(k * 0.01 + 25, 100), 2000):.2f}')

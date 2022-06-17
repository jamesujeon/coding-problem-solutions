# 문제 링크: https://www.acmicpc.net/problem/17388

scores = list(map(int, input().split()))

print('OK' if sum(scores) >= 100 else ['Soongsil', 'Korea', 'Hanyang'][scores.index(min(scores))])

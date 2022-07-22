# 문제 링크: https://www.acmicpc.net/problem/21591

wc, hc, ws, hs = map(int, input().split())

print(int(wc - ws > 1 and hc - hs > 1))

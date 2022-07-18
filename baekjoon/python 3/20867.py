# 문제 링크: https://www.acmicpc.net/problem/20867

M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

print('latmask' if L / A + M / G > R / B + M / S else 'friskus')

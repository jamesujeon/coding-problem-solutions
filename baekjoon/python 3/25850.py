# 문제 링크: https://www.acmicpc.net/problem/25850

cards = sorted((c, chr(65 + i)) for i in range(int(input())) for c in list(map(int, input().split()))[1:])
print(''.join(p for _, p in cards))

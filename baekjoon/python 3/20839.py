# 문제 링크: https://www.acmicpc.net/problem/20839

x, y, _ = map(int, input().split())
sx, sy, _ = map(int, input().split())

if sy < y / 2:
    print('E')
elif sy < y:
    print('D')
elif sx < x / 2:
    print('C')
elif sx < x:
    print('B')
else:
    print('A')

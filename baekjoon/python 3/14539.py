# 문제 링크: https://www.acmicpc.net/problem/14539

for x in range(1, int(input()) + 1):
    r, c, w, h = map(int, input().split())

    print(f"Case #{x}:")
    for _ in range(r):
        print(('+' + '-' * w) * c + '+')
        for _ in range(h):
            print(('|' + '*' * w) * c + '|')
    print(('+' + '-' * w) * c + '+')

# 문제 링크: https://www.acmicpc.net/problem/5355

for _ in range(int(input())):
    n, *ops = input().split()

    n = float(n)
    for op in ops:
        if op == '@':
            n *= 3
        elif op == '%':
            n += 5
        elif op == '#':
            n -= 7

    print(f'{n:.2f}')

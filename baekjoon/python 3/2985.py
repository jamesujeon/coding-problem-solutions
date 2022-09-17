# 문제 링크: https://www.acmicpc.net/problem/2985

a, b, c = map(int, input().split())

for op in '+-*/':
    if eval(f'{a}{op}{b}=={c}'):
        print(f'{a}{op}{b}={c}')
        break
    elif eval(f'{a}=={b}{op}{c}'):
        print(f'{a}={b}{op}{c}')
        break

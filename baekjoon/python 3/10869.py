# 문제 링크: https://www.acmicpc.net/problem/10869

a, b = map(int, input().split())
for op in ['+', '-', '*', r'//', '%']:
  print(eval(f'{a}{op}{b}'))

# 문제 링크: https://www.acmicpc.net/problem/4606

e = {' ': '0', '!': '1', '$': '4', '%': '5', '(': '8', ')': '9', '*': 'a'}

while (s := input()) != '#':
    print(''.join(f'%2{e[ch]}' if ch in e else ch for ch in s))

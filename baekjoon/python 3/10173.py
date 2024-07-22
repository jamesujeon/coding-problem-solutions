# 문제 링크: https://www.acmicpc.net/problem/10173

while (s := input()) != 'EOI':
    print('Found' if 'nemo' in s.lower() else 'Missing')

# 문제 링크: https://www.acmicpc.net/problem/1871

for _ in range(int(input())):
    L, D = input().split('-')

    L = L[::-1]
    L = sum((ord(L[i]) - 65) * 26**i for i in range(len(L)))

    print(('not ' if abs(L - int(D)) > 100 else '') + 'nice')

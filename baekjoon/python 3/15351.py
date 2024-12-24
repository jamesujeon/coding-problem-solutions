# 문제 링크: https://www.acmicpc.net/problem/15351

for _ in range(int(input())):
    print('PERFECT LIFE' if (s := sum(ord(i) - 64 for i in input() if i != ' ')) == 100 else s)

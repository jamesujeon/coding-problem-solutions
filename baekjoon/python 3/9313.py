# 문제 링크: https://www.acmicpc.net/problem/9313

while (i := int(input())) != -1:
    print(int(bin(i)[2:].zfill(32)[::-1], 2))

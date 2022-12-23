# 문제 링크: https://www.acmicpc.net/problem/3460

for _ in range(int(input())):
    print(' '.join(str(i) for i, bit in enumerate(bin(int(input()))[::-1]) if bit == '1'))

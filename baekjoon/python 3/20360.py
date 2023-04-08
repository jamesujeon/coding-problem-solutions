# 문제 링크: https://www.acmicpc.net/problem/20360

print(' '.join(str(i) for i, b in enumerate(bin(int(input()))[-1:1:-1]) if b == '1'))

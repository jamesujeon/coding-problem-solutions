# 문제 링크: https://www.acmicpc.net/problem/3622

A, a, B, b, P = map(int, input().split())
if A > B:
    A, a, B, b = B, b, A, a

print('Yes' if (B <= P and A <= b) or A + B <= P else 'No')

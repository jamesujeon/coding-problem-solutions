# 문제 링크: https://www.acmicpc.net/problem/21339

n, k = map(int, input().split())
d, s = map(int, input().split())

o = (n * d - k * s) / (n - k)
if 0 <= o and o <= 100:
    print(o)
else:
    print("impossible")

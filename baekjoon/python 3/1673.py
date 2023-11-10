# 문제 링크: https://www.acmicpc.net/problem/1673

def f():
    n, k = map(int, input().split())
    print(n + (n - 1) // (k - 1))

while True:
    try:
        f()
    except EOFError:
        break

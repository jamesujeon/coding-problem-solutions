# 문제 링크: https://www.acmicpc.net/problem/5543

def f(n):
  return min(int(input()) for _ in range(n))
print(f(3) + f(2) - 50)
# 문제 링크: https://www.acmicpc.net/problem/10872

def f(n):
  return n * f(n - 1) if n > 1 else 1

print(f(int(input())))
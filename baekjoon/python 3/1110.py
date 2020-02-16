# 문제 링크: https://www.acmicpc.net/problem/1110

n = int(input())

def calc(n):
  return (n % 10) * 10 + (n // 10 + n % 10) % 10

count = 1
m = calc(n)
while n != m:
  count += 1
  m = calc(m)

print(count)

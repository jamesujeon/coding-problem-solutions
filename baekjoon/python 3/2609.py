# 문제 링크: https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())

lcm = a * b
while a % b > 0:
    a, b = b, a % b
gcd = b
lcm //= gcd

print(gcd)
print(lcm)
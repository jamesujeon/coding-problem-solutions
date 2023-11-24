# 문제 링크: https://www.acmicpc.net/problem/2153

n = sum(ord(ch) - (38, 96)[ch.islower()] for ch in input())
for i in range(2, int(n**.5) + 1):
    if n % i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")

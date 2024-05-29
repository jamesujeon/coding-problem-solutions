# 문제 링크: https://www.acmicpc.net/problem/7789

def f(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

a, b = input().split()
print('Yes' if f(int(a)) and f(int(b + a)) else 'No')

# 문제 링크: https://www.acmicpc.net/problem/17618

def sum_digits(n):
    num = 0
    while n > 0:
        num += n % 10
        n //= 10
    return num

print(sum(i % sum_digits(i) == 0 for i in range(1, int(input()) + 1)))

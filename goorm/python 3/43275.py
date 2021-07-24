# 문제 링크: https://level.goorm.io/exam/43275/%EC%99%84%EC%A0%84%EC%88%98/quiz/1

a, b = map(int, input().split(' '))

def is_perfect(n):
    divisor_sum = sum(i + (n // i) for i in range(2, int(n**.5) + 1) if n % i == 0) + 1
    if int(n**.5) ** 2 == n:
        divisor_sum -= int(n**.5)
    return divisor_sum == n

for i in range(a, b + 1):
    if is_perfect(i):
        print(i, end=' ')
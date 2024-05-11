# 문제 링크: https://www.acmicpc.net/problem/6976

for _ in range(int(input())):
    n = int(input())
    print(n)

    i = n
    is_divisible = i == 11
    while i >= 100:
        i = i // 10 - i % 10
        is_divisible = i == 11
        print(i)

    print(f"The number {n} is {'' if is_divisible else 'not '}divisible by 11.\n")

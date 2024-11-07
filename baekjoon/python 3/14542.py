# 문제 링크: https://www.acmicpc.net/problem/14542

i = 1
while (n := int(input())) != 0:
    s = int(input())
    for _ in range(n - 2):
        m = list(map(int, input().split()))
        s += m[0] + m[-1]
    if n > 1:
        s += sum(map(int, input().split()))

    print(f"Case #{i}:{s}")
    i += 1

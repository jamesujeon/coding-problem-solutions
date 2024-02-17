# 문제 링크: https://www.acmicpc.net/problem/5100

while (N := int(input())) != 0:
    result = [0] * 5
    for _ in range(N):
        s = input()
        result[(0 if s in 'ML' else (3 if s == 'S' else 4)) if s.isalpha() else (1 if int(s) >= 12 else 2)] += 1

    print(*result)

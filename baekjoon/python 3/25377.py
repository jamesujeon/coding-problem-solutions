# 문제 링크: https://www.acmicpc.net/problem/25377

result = -1
for _ in range(int(input())):
    A, B = map(int, input().split())

    if A <= B:
        result = min(B, result) if result != -1 else B

print(result)

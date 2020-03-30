# 문제 링크: https://www.acmicpc.net/problem/10039

print(sum(map(lambda x: x if x > 40 else 40, [int(input()) for _ in range(5)])) // 5)
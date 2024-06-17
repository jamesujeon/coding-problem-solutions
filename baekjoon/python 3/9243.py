# 문제 링크: https://www.acmicpc.net/problem/9243

print(f"Deletion {'succeeded' if (all(a != b for a, b in zip(input(), input())) if int(input()) % 2 else input() == input()) else 'failed'}")

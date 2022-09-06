# 문제 링크: https://www.acmicpc.net/problem/2921

print(int(sum(i * (i + 1) for i in range(1, int(input()) + 1)) * 1.5))

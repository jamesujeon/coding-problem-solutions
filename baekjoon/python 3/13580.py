# 문제 링크: https://www.acmicpc.net/problem/13580

a, b, c = sorted(map(int, input().split()))

print('NS'[a == b or b == c or a + b == c])

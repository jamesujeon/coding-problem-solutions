# 문제 링크: https://www.acmicpc.net/problem/24606

print(2**sum(n1 != n2 for n1, n2 in zip(input(), input())))

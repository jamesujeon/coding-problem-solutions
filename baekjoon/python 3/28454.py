# 문제 링크: https://www.acmicpc.net/problem/28454

n = input()
print(sum(n <= input() for _ in range(int(input()))))

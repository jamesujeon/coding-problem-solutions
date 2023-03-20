# 문제 링크: https://www.acmicpc.net/problem/17598

print(["Tiger", "Lion"][sum(input() == "Lion" for _ in range(9)) > 4])

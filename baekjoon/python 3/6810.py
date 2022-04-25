# 문제 링크: https://www.acmicpc.net/problem/6810

result = 91 + sum(int(input()) * (3 if i % 2 else 1) for i in range(3))

print(f'The 1-3-sum is {result}')

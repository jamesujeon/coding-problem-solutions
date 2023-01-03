# 문제 링크: https://www.acmicpc.net/problem/10886

N = int(input())
cutes = sum(input() == '1' for _ in range(N))

print(f"Junhee is {'' if cutes > N // 2 else 'not '}cute!")

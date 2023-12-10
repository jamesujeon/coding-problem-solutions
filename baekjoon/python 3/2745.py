# 문제 링크: https://www.acmicpc.net/problem/2745

N, B = input().split()
B = int(B)

print(sum(B**(len(N) - i - 1) * (ord(N[i]) - 55 if N[i].isalpha() else int(N[i])) for i in range(len(N))))

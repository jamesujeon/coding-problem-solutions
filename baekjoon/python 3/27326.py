# 문제 링크: https://www.acmicpc.net/problem/27326

N = int(input())
A = list(map(int, input().split()))

for i in set(A):
    if A.count(i) == 1:
        print(i)
        break

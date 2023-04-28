# 문제 링크: https://www.acmicpc.net/problem/21679

n = int(input())
c = list(map(int, input().split()))

input()
for i in map(int, input().split()):
    c[i - 1] -= 1

for i in c:
    print("yes" if i < 0 else "no")

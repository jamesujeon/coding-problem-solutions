# 문제 링크: https://www.acmicpc.net/problem/11648

step = 0
s = input()
while len(s) > 1:
    n = 1
    for i in map(int, s):
        n *= i
    s = str(n)
    step += 1

print(step)

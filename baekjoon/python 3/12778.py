# 문제 링크: https://www.acmicpc.net/problem/12778

for _ in range(int(input())):
    _, p = input().split()
    print(*(ord(i) - 64 if p == 'C' else chr(int(i) + 64) for i in input().split()))

# 문제 링크: https://www.acmicpc.net/problem/27475

for _ in range(int(input())):
    input()
    print(len(set(map(int, input().split())) & set(map(int, input().split()))))

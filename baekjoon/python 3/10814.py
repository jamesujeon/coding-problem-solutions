# 문제 링크: https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

members_by_age = [[] for _ in range(200)]
for i in range(int(input())):
    age, name = input().split()
    members_by_age[int(age) - 1].append(f'{age} {name}')

for members in members_by_age:
    for member in members:
        print(member)
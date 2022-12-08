# 문제 링크: https://www.acmicpc.net/problem/10102

V = int(input())
A = input().count('A')
B = V - A

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")

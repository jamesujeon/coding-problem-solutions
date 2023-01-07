# 문제 링크: https://www.acmicpc.net/problem/10187

for _ in range(int(input())):
    a, b = map(float, input().split())

    print("golden" if 1.6018536501 <= a / b <= 1.6342143299 else "not")

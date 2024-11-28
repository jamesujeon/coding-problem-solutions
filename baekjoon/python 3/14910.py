# 문제 링크: https://www.acmicpc.net/problem/14910

a = -1000000
for i in map(int, input().split()):
    if a > i:
        print("Bad")
        break
    a = i
else:
    print("Good")

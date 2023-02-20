# 문제 링크: https://www.acmicpc.net/problem/16316

_ = input()
for i, word in enumerate(input().split()):
    if word != "mumble" and word != str(i + 1):
        print("something is fishy")
        break
else:
    print("makes sense")

# 문제 링크: https://www.acmicpc.net/problem/6917

while (w := input().strip()) != "quit!":
    print(w[:-1] + "ur" if len(w) > 4 and w[-3] not in "aeiouy" and w[-2:] == "or" else w)

# 문제 링크: https://www.acmicpc.net/problem/26314

for _ in range(int(input())):
    s = input()

    print(s)
    print(int(sum(s.count(v) for v in "aeiou") > len(s) // 2))

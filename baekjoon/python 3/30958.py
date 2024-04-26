# 문제 링크: https://www.acmicpc.net/problem/30958

input()
s = input()
print(max(map(s.count, map(chr, range(97, 123)))))

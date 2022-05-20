# 문제 링크: https://www.acmicpc.net/problem/15059

ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

print(max(cr - ca, 0) + max(br - ba, 0) + max(pr - pa, 0))

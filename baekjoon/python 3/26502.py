# 문제 링크: https://www.acmicpc.net/problem/26502

for _ in range(int(input())):
    print(''.join("aeiouyAEIOUY"["yaeiouYAEIOU".index(ch)] if ch in "yaeiouYAEIOU" else ch for ch in input()))

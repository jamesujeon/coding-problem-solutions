# 문제 링크: https://www.acmicpc.net/problem/10202

for _ in range(int(input())):
    c = max(map(len, ''.join(input().split()[1:]).split('O')))
    print(f"The longest contiguous subsequence of X's is of length {c}")

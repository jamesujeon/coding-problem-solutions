# 문제 링크: https://www.acmicpc.net/problem/8949

A, B = input().split()
print(''.join(str(int(a) + int(b)) for a, b in zip(A.zfill(len(B)), B.zfill(len(A)))))

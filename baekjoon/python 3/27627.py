# 문제 링크: https://www.acmicpc.net/problem/27627

S = input()
for i in range(1, len(S)):
    A, B = S[:i], S[i:]
    if A == A[::-1] and B == B[::-1]:
        print(A, B)
        break
else:
    print("NO")

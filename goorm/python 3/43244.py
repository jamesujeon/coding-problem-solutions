# 문제 링크: https://level.goorm.io/exam/43244/%EB%B6%80%EB%AA%A8-%EB%8B%A8%EC%96%B4/quiz/1

A, B = input().split()

print('YES' if set(B).issubset(set(A)) else 'NO')
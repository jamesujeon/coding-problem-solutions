# 문제 링크: https://level.goorm.io/exam/49074/파손된-램/quiz/1

N = int(input())
M = map(int, input().split())


result = [i + 1 for i, m in enumerate(M) if m & -m != m]


print(len(result))
if result:
    print(' '.join(map(str, result)))
# 문제 링크: https://level.goorm.io/exam/48757/369-%EA%B2%8C%EC%9E%84/quiz/1

N = int(input())


count = 0
for i in range(1, N):
    count += sum(s in '369' for s in str(i))


print(count)
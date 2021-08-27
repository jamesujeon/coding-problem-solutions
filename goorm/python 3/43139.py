# 문제 링크: https://level.goorm.io/exam/43139/3%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4/quiz/1

arr = [[[i * 9 + j * 3 + k + 1 for k in range(3)] for j in range(3)] for i in range(3)]


for i in range(3):
    for j in range(3):
        for k in range(3):
            print(arr[i][j][k], end=' ')
        print()
    print()
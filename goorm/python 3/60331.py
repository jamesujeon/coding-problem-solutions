# 문제 링크: https://level.goorm.io/exam/60331/%EB%B9%99%EA%B8%80%EB%B9%99%EA%B8%80-1/quiz/1

n = int(input())


arr = [[' '] * n for _ in range(n)]
i, j = 0, -1
for step in range(n):
    for _ in range(n - ((step - 1) // 2) * 2 - 1 if step > 0 else n):
        if step % 4 == 0:
            j += 1
        elif step % 4 == 1:
            i += 1
        elif step % 4 == 2:
            j -= 1
        else:
            i -= 1

        arr[i][j] = '#'


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

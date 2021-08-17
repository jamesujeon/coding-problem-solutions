# 문제 링크: https://level.goorm.io/exam/43085/insertion-sort/quiz/1

N = int(input())
arr = list(map(int, input().split()))
print_step = int(input())


step = 0
for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] >= arr[i]:
            arr[j], arr[j + 1:i + 1] = arr[i], arr[j:i]
            break

    step += 1
    if step == print_step:
        for i in arr:
            print(i, end=' ')
        break
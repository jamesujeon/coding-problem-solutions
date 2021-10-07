# 문제 링크: https://level.goorm.io/exam/43146/2%EC%B0%A8%EC%9B%90-%EA%B5%AC%EA%B0%84%ED%95%A9/quiz/1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
points = list(map(int, input().split()))


lt, rb = points[:2], points[2:]
prefix_sum = sum(sum(arr[i][lt[0]:rb[0] + 1]) for i in range(lt[1], rb[1] + 1))


print(prefix_sum)
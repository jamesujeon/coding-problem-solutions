# 문제 링크: https://level.goorm.io/exam/88520/%EB%86%80%EC%9D%B4%EA%B3%B5%EC%9B%90/quiz/1

def get_count(area, y, x, k):
    return sum(
        area[i][j] == 1
        for i in range(y, y + k)
        for j in range(x, x + k)
    )


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    counts = [
        get_count(area, i, j, k)
        for i in range(n - k + 1)
        for j in range(n - k + 1)
    ]

    print(min(counts))
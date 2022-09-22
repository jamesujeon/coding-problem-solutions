# 문제 링크: https://www.acmicpc.net/problem/4435

a_scores = [1, 2, 3, 3, 4, 10]
b_scores = [1, 2, 2, 2, 3, 5, 10]

for i in range(int(input())):
    a = sum(a_scores[j] * n for j, n in enumerate(map(int, input().split())))
    b = sum(b_scores[j] * n for j, n in enumerate(map(int, input().split())))

    result = 'No victor on this battle field'
    if a > b:
        result = 'Good triumphs over Evil'
    elif a < b:
        result = 'Evil eradicates all trace of Good'

    print(f'Battle {i + 1}: {result}')

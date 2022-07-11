# 문제 링크: https://www.acmicpc.net/problem/11257

for _ in range(int(input())):
    id, s1, s2, s3 = map(int, input().split())

    total_score = s1 + s2 + s3
    print(id, total_score, 'PASS' if total_score >= 55 and s1 >= 10.5 and s2 >= 7.5 and s3 >= 12 else 'FAIL')

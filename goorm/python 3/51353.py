# 문제 링크: https://level.goorm.io/exam/51353/%EB%B1%80%EC%9D%B4-%EC%A7%80%EB%82%98%EA%B0%84-%EC%9E%90%EB%A6%AC/quiz/1

N, M = map(int, input().split())


for i in range(N):
    if i % 2:
        print('#' + '.' * (M - 1) if (i // 2) % 2 else '.' * (M - 1) + '#')
    else:
        print('#' * M)
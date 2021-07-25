# 문제 링크: https://level.goorm.io/exam/43263/%ED%8A%B9%EC%A0%95-%EA%B5%AC%EA%B0%84%EC%9D%98-%ED%95%A9/quiz/1

input()
arr = list(map(int, input().split()))
i, j = map(int, input().split())

print(sum(arr[i - 1:j]))
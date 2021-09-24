# 문제 링크: https://level.goorm.io/exam/43181/%ED%94%BC%EB%9D%BC%EB%AF%B8%EB%93%9C/quiz/1

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (i * 2 - 1))

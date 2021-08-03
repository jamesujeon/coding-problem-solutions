# 문제 링크: https://level.goorm.io/exam/43118/1%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

N = int(input())

b1 = bin(N).count('1')
b2 = bin(int(str(N), 16)).count('1')

print(b1, b2)
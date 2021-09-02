# 문제 링크: https://level.goorm.io/exam/49088/%EC%9D%98%EC%A2%8B%EC%9D%80-%ED%98%95%EC%A0%9C/quiz/1

N1, N2 = map(int, input().split())
D = int(input())


for i in range(D):
    is_odd = N1 % 2
    N1 //= 2
    N2 += N1 + is_odd

    N1, N2 = N2, N1

if D % 2:
    N1, N2 = N2, N1


print(N1, N2)
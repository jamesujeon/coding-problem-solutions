# 문제 링크: https://www.acmicpc.net/problem/25640

mbti = input()
print(sum(input() == mbti for _ in range(int(input()))))

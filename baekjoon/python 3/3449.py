# 문제 링크: https://www.acmicpc.net/problem/3449

for _ in range(int(input())):
    print(f'Hamming distance is {sum(i != j for i, j in zip(input(), input()))}.')

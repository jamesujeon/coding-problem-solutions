# 문제 링크: https://www.acmicpc.net/problem/10871

_, x = map(int, input().split())

small_nums = [str(i) for i in map(int, input().split()) if i < x]

print(' '.join(small_nums))
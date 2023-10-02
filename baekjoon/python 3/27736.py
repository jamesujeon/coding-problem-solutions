# 문제 링크: https://www.acmicpc.net/problem/27736

N = int(input())
votes = list(map(int, input().split()))

if votes.count(0) >= N / 2:
    print("INVALID")
elif sum(votes) > 0:
    print("APPROVED")
else:
    print("REJECTED")

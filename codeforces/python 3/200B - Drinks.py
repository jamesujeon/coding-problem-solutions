# 문제 링크: http://codeforces.com/problemset/problem/200/B

_ = input()
volumes = list(map(int, input().split()))

print(sum(volumes) / len(volumes))
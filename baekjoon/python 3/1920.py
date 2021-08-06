# 문제 링크: https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

input()
n = list(map(int, input().split()))
input()
m = list(map(int, input().split()))


n.sort()

def contains(num):
    low, high = 0, len(n) - 1
    while low <= high:
        mid = (low + high) // 2
        if n[mid] < num:
            low = mid + 1
        elif n[mid] > num:
            high = mid - 1
        else:
            return True

    return False


for num in m:
    print(int(contains(num)))
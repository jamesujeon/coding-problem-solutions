# 문제 링크: https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

def merged(left: [int], right: [int]) -> [int]:
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    return arr + left[i:] + right[j:]

def sorted(arr: [int]) -> [int]:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    return merged(sorted(arr[:mid]), sorted(arr[mid:]))

for num in sorted([int(input()) for _ in range(int(input()))]):
    print(num)
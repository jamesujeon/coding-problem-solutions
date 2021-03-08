# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12953

from fractions import gcd

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer *= arr[i] // gcd(answer, arr[i])
    return answer
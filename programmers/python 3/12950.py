# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[c1 + c2 for c1, c2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]
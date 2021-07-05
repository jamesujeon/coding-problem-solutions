# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    return [str(bin(r1 | r2)[2:]).zfill(n).replace('1', '#').replace('0', ' ') for r1, r2 in zip(arr1, arr2)]
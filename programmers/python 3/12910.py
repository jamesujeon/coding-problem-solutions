# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    return sorted(n for n in arr if n % divisor == 0) or [-1]
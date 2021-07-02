# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    count = 0
    i = n
    while sum(i) >= n:
        j = i - 1
        while sum(i) - sum(j) < n:
            j -= 1
        if sum(i) - sum(j) == n:
            count += 1
        i -= 1

    return count

def sum(n):
    return (n * (n + 1)) // 2
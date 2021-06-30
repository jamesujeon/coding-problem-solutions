# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()

    l, r = 0, len(people) - 1
    count = 0
    while l <= r:
        weight = people[r]
        if weight + people[l] <= limit:
            l += 1
        r -= 1
        count += 1

    return count
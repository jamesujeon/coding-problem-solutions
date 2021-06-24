# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    if not numbers:
        return 1 if target == 0 else 0

    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = sum(
                arr1[i][k] * arr2[k][j]
                for k in range(len(arr2))
            )
    return answer
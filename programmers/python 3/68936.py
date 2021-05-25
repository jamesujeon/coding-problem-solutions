# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68936

from typing import List

def solution(arr):
    def compress(size, y, x):
        if all(arr[i][j] == arr[y][x] for i in range(y, y + size) for j in range(x, x + size)):
            return [0, 1] if arr[y][x] else [1, 0]
        else:
            size //= 2
            return [
                sum(results) for results in zip(
                    compress(size, y, x),
                    compress(size, y, x + size),
                    compress(size, y + size, x),
                    compress(size, y + size, x + size)
                )
            ]

    return compress(len(arr), 0, 0)
# 문제 링크: https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
        for i in range(len(matrix)):
            min_value = min(matrix[i])
            min_index = matrix[i].index(min_value)
            max_value = max(row[min_index] for row in matrix)
            if min_value == max_value:
                lucky_nums.append(max_value)

        return lucky_nums
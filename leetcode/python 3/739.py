# 문제 링크: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            j = 1
            while T[i] >= T[i + j]:
                if not result[i + j]:
                    j = 0
                    break
                j += result[i + j]
            result[i] = j
        return result
# 문제 링크: https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:        
        degrees, max_degree = {}, 0
        for i, num in enumerate(nums):
            if num not in degrees:
                degrees[num] = [0, i, i]
            degrees[num][0] += 1
            degrees[num][2] = i

            if degrees[num][0] > max_degree:
                max_degree = degrees[num][0]

        return min(degree[2] - degree[1] + 1 for degree in degrees.values() if degree[0] == max_degree)
# 문제 링크: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def dfs(depth: int):
            if depth == len(nums) - 1:
                permutations.append(nums[:])

            for i in range(depth, len(nums)):
                nums[depth], nums[i] = nums[i], nums[depth]
                dfs(depth + 1)
                nums[depth], nums[i] = nums[i], nums[depth]

        dfs(0)
        return permutations
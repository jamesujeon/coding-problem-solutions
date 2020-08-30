# 문제 링크: https://leetcode.com/problems/subsets/

# 제곱 이용
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, subsets = len(nums), []
        for i in range(2**n):
            digits = bin(i)[2:].zfill(n)
            subsets.append([])
            for j in range(n):
                if digits[j] == '1':
                    subsets[-1] += [nums[j]]
        return subsets

# 재귀 이용
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        others = self.subsets(nums[1:])
        return [[nums[0]] + subset for subset in others] + others
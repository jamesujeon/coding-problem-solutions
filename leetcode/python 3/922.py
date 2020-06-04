# 문제 링크: https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums = [[], []]
        for i in A:
            nums[i % 2].append(i)
        return [nums[i % 2].pop() for i in range(len(A))]

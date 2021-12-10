# 문제 링크: https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list((set(nums1) & set(nums2)) | (set(nums2) & set(nums3)) | (set(nums1) & set(nums3)))
# 문제 링크: https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_index = arr.index(max(arr))

        return (
            0 < peak_index < len(arr) - 1 and
            all(arr[i] < arr[i + 1] for i in range(peak_index)) and
            all(arr[i] > arr[i + 1] for i in range(peak_index, len(arr) - 1))
        )
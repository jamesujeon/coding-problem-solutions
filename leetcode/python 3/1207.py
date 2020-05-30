# 문제 링크: https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = []
        for i in set(arr):
            occurrence = arr.count(i)
            if occurrence in occurrences:
                return False
            occurrences.append(occurrence)
        return True

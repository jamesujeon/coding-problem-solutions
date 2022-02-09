# 문제 링크: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_indexes = [i for i, box in enumerate(boxes) if box == '1']

        return [sum(abs(i - j) for j in one_indexes) for i in range(len(boxes))]

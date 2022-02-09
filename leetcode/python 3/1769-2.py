# 문제 링크: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        count = ops = 0
        for i in range(len(boxes)):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        count = ops = 0
        for i in range(len(boxes) - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        return answer

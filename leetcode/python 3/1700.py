# 문제 링크: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if not counts[sandwich]:
                break
            counts[sandwich] -= 1
        return sum(counts)
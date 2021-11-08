# 문제 링크: https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = ['type', 'color', 'name'].index(ruleKey)
        return sum(item[i] == ruleValue for item in items)
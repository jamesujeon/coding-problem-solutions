# 문제 링크: https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        max_power = count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                if count > max_power:
                    max_power = count
            else:
                count = 1
        return max_power

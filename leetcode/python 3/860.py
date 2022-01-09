# 문제 링크: https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        moneys = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                moneys[5] += 1
            elif bill == 10:
                moneys[5] -= 1
                moneys[10] += 1
            elif bill == 20:
                if moneys[10] > 0:
                    moneys[5] -= 1
                    moneys[10] -= 1
                else:
                    moneys[5] -= 3

            if moneys[5] < 0:
                return False

        return True
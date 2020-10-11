# 문제 링크: https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day_of_month[2] += 1
        return sum(day_of_month[:month]) + day
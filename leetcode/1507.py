# 문제 링크: https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        date = date.split()
        return f'{date[2]}-{str(months.index(date[1]) + 1).zfill(2)}-{date[0][:-2].zfill(2)}'

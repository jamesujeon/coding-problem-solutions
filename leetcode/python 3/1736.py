# 문제 링크: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)

        for i, ch in enumerate(time):
            if ch == '?':
                if i == 0:
                    time[i] = '2' if time[1] in '0123?' else '1'
                elif i == 1:
                    time[i] = '9' if time[0] in '01' else '3'
                elif i == 3:
                    time[i] = '5'
                elif i == 4:
                    time[i] = '9'

        return ''.join(time)

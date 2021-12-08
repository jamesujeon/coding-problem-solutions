# 문제 링크: https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration, key = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                key = keysPressed[i]
            elif duration == max_duration:
                key = max(keysPressed[i], key)

        return key
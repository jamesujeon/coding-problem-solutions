# 문제 링크: https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        for box in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            boxes = min(box[0], truckSize)
            units += boxes * box[1]
            truckSize -= boxes
            if truckSize == 0:
                break
        return units
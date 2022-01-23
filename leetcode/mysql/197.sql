-- 문제 링크: https://leetcode.com/problems/rising-temperature/

SELECT W.id
FROM Weather AS W
JOIN Weather AS Y ON Y.recordDate = DATE_SUB(W.recordDate, INTERVAL 1 DAY)
WHERE Y.temperature < W.temperature
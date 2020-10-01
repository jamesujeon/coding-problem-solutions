-- 문제 링크: https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT e.Name AS Employee
FROM Employee AS e
JOIN Employee AS m ON m.Id = e.ManagerId
WHERE e.Salary > m.Salary

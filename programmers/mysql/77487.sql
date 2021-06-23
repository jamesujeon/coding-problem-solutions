-- 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77487

SELECT *
FROM PLACES P
WHERE EXISTS (
    SELECT 1
    FROM PLACES
    WHERE HOST_ID = P.HOST_ID
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) > 1
)
ORDER BY ID ASC
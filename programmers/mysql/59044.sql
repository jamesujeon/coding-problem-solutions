-- 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/59044

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY DATETIME ASC
LIMIT 3

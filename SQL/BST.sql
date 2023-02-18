--https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

SELECT N, 
       CASE WHEN P is NULL THEN 'Root'
            WHEN N IN (SELECT DISTINCT P FROM BST) THEN 'Inner'
            ELSE 'Leaf' END
FROM BST
ORDER BY N
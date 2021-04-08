// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12950

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    zip(arr1, arr2).map { zip($0, $1).map(+) }
}
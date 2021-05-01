// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12949

func solution(_ arr1: [[Int]], _ arr2: [[Int]]) -> [[Int]] {
    arr1.indices.map { i in
        arr2[0].indices.map { j in
            arr2.indices
                .map { k in arr1[i][k] * arr2[k][j] }
                .reduce(0, +)
        }
    }
}
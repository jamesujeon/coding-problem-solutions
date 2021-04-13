// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12944

func solution(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0, +)) / Double(arr.count)
}
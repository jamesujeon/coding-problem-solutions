// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12935

func solution(_ arr:[Int]) -> [Int] {
    guard arr.count > 1,
          let min = arr.min(),
          let minIndex = arr.firstIndex(of: min)
    else { return [-1] }

    var arr = arr
    arr.remove(at: minIndex)
    return arr
}
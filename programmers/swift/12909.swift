// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12909

func solution(_ s:String) -> Bool {
    var count = 0
    for bracket in s where count >= 0 {
        count += bracket == "(" ? 1 : -1
    }

    return count == 0
}
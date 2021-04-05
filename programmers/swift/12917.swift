// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12917

func solution(_ s:String) -> String {
    return String(s.sorted { $0 > $1 })
}
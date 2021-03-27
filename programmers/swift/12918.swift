// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12918

func solution(_ s:String) -> Bool {
    return [4, 6].contains(s.count) && Int(s) != nil
}
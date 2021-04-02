// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12919

func solution(_ s:String) -> String {
    let startIndex = String.Index(utf16Offset: (s.count - 1) / 2, in: s)
    let endIndex = String.Index(utf16Offset: s.count / 2 + 1, in: s)
    
    return String(s[startIndex..<endIndex])
}
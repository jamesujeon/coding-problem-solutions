// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12915

func solution(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted {
        let n0 = $0[String.Index(utf16Offset: n, in: $0)]
        let n1 = $1[String.Index(utf16Offset: n, in: $1)]
        return n0 == n1 ? $0 < $1 : n0 < n1
    }
}
// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12926

func solution(_ s:String, _ n:Int) -> String {
    return String(s.map { ch in
        guard ch != " " else { return ch }

        let base = ch.isUppercase ? 65 : 97
        let encrypted = (Int(ch.asciiValue!) - base + n) % 26 + base

        if let scalar = Unicode.Scalar(encrypted) {
            return Character(scalar)
        } else {
            return ch
        }
    })
}
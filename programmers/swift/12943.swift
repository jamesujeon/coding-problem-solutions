// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12943

func solution(_ num:Int) -> Int {
    var num = num
    for count in 0 ..< 500 {
        if num == 1 {
            return count
        }

        num = num % 2 == 0 ? num / 2 : num * 3 + 1
    }
    return -1
}
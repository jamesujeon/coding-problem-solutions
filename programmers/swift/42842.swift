// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42842

func solution(_ brown: Int, _ yellow: Int) -> [Int] {
    var (width, height) = (0, 2)
    while width * height != brown + yellow {
        height += 1
        width = (brown - 2 * height + 4) / 2
    }

    return [width, height]
}
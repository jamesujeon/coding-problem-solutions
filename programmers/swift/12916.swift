// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12916

import Foundation

func solution(_ s:String) -> Bool {
    let lowercased = s.lowercased()
    return lowercased.filter({ $0 == "p" }).count == lowercased.filter({ $0 == "y" }).count
}
// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12969

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }

print(String(repeating: String(repeating: "*", count: n[0]) + "\n", count: n[1]))
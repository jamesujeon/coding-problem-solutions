// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72410

import Foundation

extension String {

    subscript(range: PartialRangeUpTo<Int>) -> String {
        String(self[..<index(startIndex, offsetBy: range.upperBound)])
    }

    func replacing(regex pattern: String, with replacement: String) -> String {
        replacingOccurrences(
            of: pattern,
            with: replacement,
            options: [.regularExpression]
        )
    }
}

func solution(_ new_id:String) -> String {
    var new_id = new_id.lowercased()
        .replacing(regex: "[^a-z0-9-_.]", with: "")
        .replacing(regex: "[.]{2,}", with: ".")
        .replacing(regex: "^[.]|[.]$", with: "")

    if new_id.isEmpty {
        new_id = "aaa"
    } else {
        new_id = new_id[..<min(new_id.count, 15)]
            .replacing(regex: "[.]$", with: "")

        if new_id.count < 3 {
            new_id = new_id.padding(
                toLength: 3,
                withPad: String(new_id.last ?? Character("")),
                startingAt: 0
            )
        }
    }

    return new_id
}
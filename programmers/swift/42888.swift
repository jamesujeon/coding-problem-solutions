// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42888

import Foundation

func solution(_ record: [String]) -> [String] {
    var users = Dictionary<String, String>()
    var messages = Array<(String, String)>()
    for command in record {
        let arguments = command.components(separatedBy: " ")
        if ["Enter", "Change"].contains(arguments[0]) {
            users[arguments[1]] = arguments[2]
        }

        if arguments[0] == "Enter" {
            messages.append((arguments[1], "님이 들어왔습니다."))
        } else if arguments[0] == "Leave" {
            messages.append((arguments[1], "님이 나갔습니다."))
        }
    }

    return messages.map { users[$0]! + $1 }
}
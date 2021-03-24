// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12901

func solution(_ a: Int, _ b: Int) -> String {
    let weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    let daysOfMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return weekdays[(daysOfMonth[..<a].reduce(0, +) + b + 4) % 7]
}
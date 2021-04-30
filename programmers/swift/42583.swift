// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42583

func solution(_ bridgeLength: Int, _ weight: Int, _ truckWeights: [Int]) -> Int {
    var seconds = 0
    var bridge = [[Int]]()
    var truckWeights = truckWeights

    while !bridge.isEmpty || !truckWeights.isEmpty {
        bridge.indices.forEach {
            bridge[$0][1] += 1
        }
        if let truckWeight = bridge.first?.last, truckWeight >= bridgeLength {
            bridge.removeFirst()
        }

        let threshold = weight - bridge.map { $0[0] }.reduce(0, +)
        if let truckWeight = truckWeights.first, truckWeight <= threshold {
            bridge.append([truckWeights.removeFirst(), 0])
        }

        seconds += 1
    }

    return seconds
}
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    while truck_weights or bridge:
        for truck in bridge:
            truck[1] += 1
        if bridge and bridge[0][1] >= bridge_length:
            bridge.pop(0)

        threshold = weight - sum(truck[0] for truck in bridge)
        if truck_weights and truck_weights[0] <= threshold:
            bridge.append([truck_weights.pop(0), 0])

        answer += 1

    return answer
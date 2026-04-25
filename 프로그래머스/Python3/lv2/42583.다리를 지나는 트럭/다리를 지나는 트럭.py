def solution(bridge_length, can_holding_weight, trucks):
    answer = 0
    bridge = []
    net_weights = 0
    while trucks:
        if net_weights + trucks[0] <= can_holding_weight:
            entranceTruck = trucks.pop(0)
            bridge.append([entranceTruck, bridge_length])
            net_weights += entranceTruck
        if bridge:
            answer += 1
            for i in range(len(bridge)):
                bridge[i][1] -= 1
            if bridge[0][1] == 0:
                escapeTruck = bridge.pop(0)
                net_weights -= escapeTruck[0]
    return answer + bridge_length
# while bridge : # 이게 뭔지 모르겠음
# 저렇게 조건을 쓰면 list가 비는 순간 멈추는 것 같음
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    sec = 0
    print(sum(bridge))
    while bridge :
        bridge.pop(0)
        sec += 1
        if truck_weights :
            if sum(bridge) + truck_weights[0] <= weight :
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return sec

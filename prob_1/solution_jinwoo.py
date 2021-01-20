def solution(bridge_length, weight, truck_weights):

    sec = 0
    bridge = [0] * bridge_length
    w = 0
    while truck_weights:
        left_truck = bridge.pop(0)
        if w + truck_weights[0] - left_truck <= weight:
            w = w + truck_weights[0] - left_truck
            bridge.append(truck_weights.pop(0))
        else:
            w = w - left_truck
            bridge.append(0)
        sec += 1
    
    return sec + bridge_length
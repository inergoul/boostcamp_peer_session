from queue import deque
def solution(bridge_length, weight, truck_weights):
    ans = 1
    truck_weights = deque(truck_weights)
    bridge = deque([[truck_weights.popleft(), bridge_length]])
    bridge_weight = bridge[-1][0]
    while truck_weights:
        truck = 0
        if bridge and truck_weights[0] + bridge_weight > weight:
            truck = bridge.popleft()
            bridge_weight -= truck[0]
            ans += truck[1]
            for arr in bridge:
                arr[1] -= truck[1]
        if truck_weights and truck_weights[0] + bridge_weight <= weight:
            if not truck:
                for arr in bridge:
                    arr[1] -= 1
                if bridge and bridge[0][1] == 0:
                    w = bridge.popleft()[0]
                    bridge_weight -= w
                ans += 1
            bridge.append([truck_weights.popleft(), bridge_length])
            bridge_weight += bridge[-1][0]
    return ans + bridge[-1][1]
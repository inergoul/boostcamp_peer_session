from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wait_truck = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    while len(bridge):
        time+=1
        bridge.popleft()
        if len(wait_truck):
            if sum(bridge)+wait_truck[0]<=weight:
                bridge.append(wait_truck.popleft())
            else:
                bridge.append(0)
    return time
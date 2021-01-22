from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_remain = deque(truck_weights)
    times = deque()    
    step = 0
    idx = 0
    in_bridge = 0
    
    # 보낼 트럭이 남아있거나, 가고있는 차가 있으면 반복
    while truck_remain or in_bridge:
        step += 1
        times = deque(map(lambda x:x+1, times))
        
        # 1. 보낼 트럭이 남아있으면
        if truck_remain:
            if in_bridge + truck_remain[0] <= weight:
                in_bridge += truck_remain.popleft()
                times.append(1)
        
        # 2. 도착한 트럭이 있으면
        if times[0] == bridge_length:
            times.popleft()
            in_bridge -= truck_weights[idx]
            idx += 1
    else:
        step += 1 
    
    return step
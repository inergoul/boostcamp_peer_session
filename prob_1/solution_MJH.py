def solution(bridge_length, weight, truck_weights):
    t = 0           # 트럭의 탑승시점
    passing = []    # 다리 위의 트럭 리스트
    pass_time = []  # 각 트럭들의 탑승시점 리스트
    while truck_weights:
        if t != 0 and pass_time[0]+bridge_length==t:    # 타임0일 때에는 리스트 원소가 없음 and 탑승시점+다리길이=내릴 시점
            passing.pop(0)
            pass_time.pop(0)    # 트럭이 다리를 빠져나갈 때, 해당 트럭의 t도 pop!
        if truck_weights[0] + sum(passing) <= weight: # 다음 트럭을 합해도 무게제한을 넘지 않는다면 append
            passing.append(truck_weights.pop(0))    # pop 메소드 후 바로 append
            pass_time.append(t)
        t += 1
    return t+bridge_length
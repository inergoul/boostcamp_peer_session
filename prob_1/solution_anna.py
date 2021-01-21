def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 1
    on = 0
    q = []
    for truck in truck_weights:
        while len(q) and (on + truck > weight):
            on -= q[0][1]
            time = max(time, q[0][0] + bridge_length)
            q.pop(0)
        on += truck
        q.append([time, truck])
        time += 1
    answer = max(answer, q[-1][0] + bridge_length)
    return answer

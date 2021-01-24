from collections import defaultdict

def solution(participant, completion):
    running = defaultdict(int)
    for name in participant:
        running[name] += 1
    for name in completion:
        running[name] -= 1
        if running[name] == 0:
            #running.pop(name, None)
            del running[name]
    return list(running.keys())[0]

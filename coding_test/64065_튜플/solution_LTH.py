def solution(s):
    string = list(map(lambda x:set(x.split(',')), s[2:-2].split('},{')))
    string.sort(key = lambda x:len(x))
    ans = []
    prev = set()
    for i in string:
        ans.append(int((i - prev).pop()))
        prev = i
    return ans
# 3, 5 => 8 / 15
# 4, 5 => 12 / 20
# 3, 4 => 6 / 12
# 2, 3 => 2 / 6
def solution(w,h):
    gcd = get_gcd(w, h)
    x = w // gcd
    y = h // gcd
    remain = (x-1) * (y-1)
    sliced = x*y - remain
    repeat = w // x
    answer = (w*h) - (repeat*sliced)
    return answer

def get_gcd(w, h):
    while h:
        w, h = h, w % h
    return w
def solution(w, h):
    slope = h / w
    gcd = GCD(w, h)
    return w * h - h - w + gcd

def GCD(w, h):
    if w % h == 0:
        return h
    return GCD(h, w % h) if w > h else GCD(h, w)
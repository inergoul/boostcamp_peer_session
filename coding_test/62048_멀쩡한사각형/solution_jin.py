def solution(w,h):
    # 최대공약수 반환 함수
    def _gcd(a,b):
        if b%a == 0:
            return a
        else:
            return _gcd((b%a), a)
    # 잘리는 직사각형의 개수
    cut = w + h - _gcd(w,h)  
    return w*h - cut
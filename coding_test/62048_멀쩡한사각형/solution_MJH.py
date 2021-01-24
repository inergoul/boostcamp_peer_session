def solution(w,h):
    cdg = max(i for i in range(1,min(w,h)+1) if w%i==0 and h%i==0)
    return w*h-int((w/cdg+h/cdg-1)*cdg)
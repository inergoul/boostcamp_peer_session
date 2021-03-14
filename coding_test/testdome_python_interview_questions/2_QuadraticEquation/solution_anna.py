import math

def find_roots(a, b, c):
    return ((-b + math.sqrt(b*b - 4*a*c)) / (2*a), (-b - math.sqrt(b*b - 4*a*c)) / (2*a))

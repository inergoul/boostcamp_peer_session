from math import sqrt
def find_roots(a, b, c):
    return (-b + sqrt(b **2 - 4 *a* c)) / 2/a, (-b - sqrt(b **2 - 4 *a* c)) / 2/a

print(find_roots(2, 10, 8))
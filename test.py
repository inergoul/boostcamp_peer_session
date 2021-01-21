# numbers = [1,2,3,4,5,6]
# a = (x * x for x in numbers)
# print(a)

# def generator():
#     yield 0
#     yield 1
#     yield 2

# g = generator()
# a = next(g)
# print(a)
# b = next(g)
# print(b)

# L = [1,2,3]
# print(L.__iter__())


# def generate_power(exponent):
#     def wrapper(f):
#         def inner(*args):
#             result = f(*args)
#             print(">>>>>", result)
#             return exponent ** result
#         return inner
#     return wrapper

# @generate_power(3)
# def raise_two(n):
#     return n**2

# print(raise_two(5))
# raise_two(2)



def raise_two(n):
    return n**2
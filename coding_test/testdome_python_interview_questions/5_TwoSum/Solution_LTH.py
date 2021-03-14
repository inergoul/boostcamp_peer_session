from bisect import bisect_left
from collections import defaultdict
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    location = defaultdict(list)
    
    for idx, num in enumerate(numbers):
        location[num].append(idx)
        
    numbers.sort()
    
    for i in numbers:
        idx1 = location[i][0]
        a = target_sum - i
        flag = False
        if a in location:
            for idx2 in location[a]:
                if idx2 != idx1:
                    return idx1, idx2
        

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
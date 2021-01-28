from bisect import bisect_left
def count_numbers(sorted_list, less_than):
    n = len(sorted_list)
    idx = bisect_left(sorted_list, less_than)
    return idx

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2
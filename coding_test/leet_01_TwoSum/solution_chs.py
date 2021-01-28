class Solution(object):
    def twoSum(self, nums, target):
        for i,num_1 in enumerate(nums):
            for j,num_2 in enumerate(nums):
                if num_1+num_2 == target and i != j:
                    return [i,j]
        
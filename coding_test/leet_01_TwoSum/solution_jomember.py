class Solution:

    def twoSum1(self, nums, target):
        '''
        Runtime : 80ms
        Memory Usage : 14.3MB
        '''
        for i in range(len(nums)):
            num = target-nums[i]
            for j in range(i+1,len(nums)):
                if num==nums[j]:
                    return [i,j]

    
    def twoSum2(self, nums, target):
        '''
        Rumtime :80ms
        Memory Usage : 14.5MB
        '''
        for i in range(len(nums)):
            num = target-nums[i]
            if num in nums[i+1:]:
                return [i,nums[i+1:].index(num)+i+1]
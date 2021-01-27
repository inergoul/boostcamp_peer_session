class Solution:

    # brute force (time 48ms / memory 14.5MB)
    # time O(n^2) / space O(1)

    def twoSum1(self, nums, target):
        Flag = True
        fr = 0
        to = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    fr = i
                    to = j
                    Flag = False
                    break
            if Flag == False:
                break

        return [fr, to]

    # brute force (time 36ms / memory 14.5MB)
    # time O(n^2) / space O(1)

    def twoSum2(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
    
    # hash table (time 68ms / memory 14.3MB)
    # time O(n) / space O(n)

    def twoSum3(self, nums, target):
        
        hashmap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i
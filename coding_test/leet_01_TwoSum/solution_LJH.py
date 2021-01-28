class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
    # 아래 잘못품
    # def twoSum(self, nums, target):
    #     tmp = [0 for _ in range(len(nums))]
    #     tmp_sum = 0
    #     for i in range(1 << len(nums)):
    #         for j in range(len(nums)):
    #             if i & (1<<j):
    #                 tmp_sum += nums[j]
    #                 tmp[j] = 1
    #         # target과 같아지면
    #         if target == tmp_sum:
    #             break

    #         # 아니면 반복
    #         else:
    #             tmp = [0 for _ in range(len(nums))]
    #             tmp_sum = 0
                
    #     answer = []
    #     for idx, k in enumerate(tmp):
    #         if k == 1:
    #             answer.append(idx)
    #     return answer
  
nums = [3,2,4]
target = 6

ts = Solution()
print(ts.twoSum(nums=nums, target=6))
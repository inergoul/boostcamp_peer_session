from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [0, 0]
        cnt = defaultdict(list)
        for i, n in enumerate(nums):
            cnt[n].append(i)
        for n in list(set(nums)):
            if len(cnt[n]) and len(cnt[target - n]):
                if (target - n == n) and (len(cnt[n]) > 1):
                    answer[0] = cnt[n][0]
                    answer[1] = cnt[n][1]
                elif target - n != n:
                    answer[0] = cnt[n][0]
                    answer[1] = cnt[target - n][0]
        return answer

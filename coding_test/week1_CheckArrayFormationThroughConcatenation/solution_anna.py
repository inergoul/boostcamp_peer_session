class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for i, p in enumerate(pieces):
            same = False
            for j, a in enumerate(arr):
                if (a == p[0]):
                    same = True
                    for k in range(len(p)):
                        if (arr[j + k] != p[k]):
                            return False
            if not same:
                return False
        return True

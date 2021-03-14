class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        check_num = {num:idx for idx, num in enumerate(arr)}

        for piece in pieces: # pieces에서 하나씩 확인

            #piece 의 처음과 끝이 arr에 있는지 확인
            if piece[0] not in check_num or piece[-1] not in check_num:
                return False

            check = arr[check_num[piece[0]]:check_num[piece[-1]] + 1]

            if piece != check:
                return False

        return True
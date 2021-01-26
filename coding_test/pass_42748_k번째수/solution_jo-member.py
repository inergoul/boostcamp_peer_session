def solution(array, commands):
    ans = []
    for c in commands:
        i,j,k = c
        s_array = array[i-1:j]
        s_array.sort()
        ans.append(s_array[k-1])
    print(ans)
    return ans
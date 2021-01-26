def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr = [0, 0, 0]
    for num in range(len(answers)):
        if answers[num] == one[num % len(one)]:
            arr[0] += 1
        if answers[num] == two[num % len(two)]:
            arr[1] += 1
        if answers[num] == three[num % len(three)]:
            arr[2] += 1
    ans = [i + 1 for i in range(3) if arr[i] == max(arr)]
    return ans
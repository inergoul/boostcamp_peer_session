def solution(phone_book):
    # 정렬한 후 하나의 원소가 뒤쪽 원소로 시작하는 경우 False
    # Time : O(NlogN) - 정렬
    book = sorted(phone_book)
    for i, num in enumerate(book):
        for j in range(i+1, len(book)):
            if num == book[j][:len(str(num))]:
                return False
    return True
    
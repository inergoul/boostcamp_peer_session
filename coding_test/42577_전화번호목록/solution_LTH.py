def solution(phone_book):
    phone_book.sort()
    prev = '-'
    for number in phone_book:
        if number.startswith(prev):
            return False
        prev = number
    return True
from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book_dict = defaultdict(lambda: 0)

    for number in phone_book:
        phone_book_dict[number] = 1

    for idx, number in enumerate(phone_book):
        string = ""
        for char in number:
            string += char
            if phone_book_dict[string] == 1 and string != phone_book[idx]:
                answer = False

    return answer
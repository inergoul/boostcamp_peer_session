from collections import deque
def solution(board, moves):
    box = deque()
    answer =0
    for action in moves:
        for i in range(len(board)):
            if board[i][action-1]!=0:
                new_item = board[i][action-1]
                if len(box)!=0:
                    last_item = box.pop()
                    if last_item ==new_item:
                        answer +=2
                    else:
                        box.append(last_item)
                        box.append(new_item)
                else:
                    box.append(new_item)
                board[i][action-1] = 0
                break
    return answer
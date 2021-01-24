def solution(board, moves):
    answer = 0
    row = len(board)
    col = len(board[0])
    idx = [row for i in range(col)]
    for c in range(col):
        for r in range(row):
            if board[r][c]:
                idx[c] = r
                break;
    basket = []
    for m in moves:
        if idx[m - 1] < row:
            if basket and basket[-1] == board[idx[m - 1]][m - 1]:
                answer += 2
                basket.pop()
            else:
                basket.append(board[idx[m - 1]][m - 1])
            idx[m - 1] += 1
    return answer

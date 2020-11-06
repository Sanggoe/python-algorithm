def solution(board, moves):
    # stack 배열 초기화
    stack_board = []
    for _ in range(len(board)):
        stack_board.append(list())

    # stack 배열에 board 값 넣기
    for line in board[::-1]:
        for i in range(len(board)):
            if line[i]:
                stack_board[i].append(line[i])

    print(stack_board)


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
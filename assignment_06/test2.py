import numpy as np
import random

a = np.array([['-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-'],
              ['-', '1', '-', '-', '-', '-', '-']])


def score_position(board,piece):
        board = list(board)
        rows =  len(board)  
        cols =  len(board[0])
        score = 0
        for r in range(rows):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(cols -3):
                window = row_array[c:c+4]
                if window.count(piece) == 4:
                    score += 100
                elif (window.count(piece) == 3) or (window.count(piece) == 2):
                    score += 10
        return score


def get_next_open_row(board, col):
    board = list(board)
    rows =  len(board)
    for r in range(rows):
        if board[r][col] == 0:
            return r

def is_valid_location(board,col):
    board = list(board)
    rows =  len(board)
    return board[rows-1][col] == '-'

def get_valid_location(board):
    board = list(board)
    cols =  len(board[0])
    valid_location = []
    print(board)
    print(type(board))
    print(cols)
    for col in range(cols):
        if is_valid_location(board,col):
            valid_location.append(col)

    return valid_location


def get_next_open_row(board, col):
    board = list(board)
    rows =  len(board)
    for r in range(rows):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    return board

def pick_best_move(board, piece):

    valid_location = get_valid_location(board)
    print("yup",valid_location)
    best_score = 0
    best_col = random.choice(valid_location)
    for col in valid_location:
            row = get_next_open_row(board,col)
            temp_board = board.copy()
            drop_piece(temp_board,row, col,piece)
            score = score_position(temp_board,piece)
            if score > best_score:
                best_score = score
                best_col = col

    return best_col
import numpy as np
def convert(a):
    board = a.copy()
    board  = np.where(a==0, '-', a)
    board  = np.where(a==1, 'x', a)
    print(board)

a = np.array([[0,0,0,0,0],
              [0,1,0,0,1]])
convert(a)
# # to_list(a)
# # print(list(a))
# pick_best_move(a,1)
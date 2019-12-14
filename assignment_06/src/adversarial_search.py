#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-12-14 13:53:52.203630

@author: Manoj Kolpe Lingappa
"""

import argparse
import timeit
from helper import *

PLAYER_PIECE = 1
AI_PIECE = 2
alpha = -float('inf')
beta = float('inf')

def play_game(game, rows, columns):
    """Function to start playing the game.
    Here you will have to create two players
    * Human
    * AI agent
    Both of these players should be given alternate turns
    to play the game.
    Each step SHOULD BE PRINTED on the console.
    If an invalid position (already occupied position) is
    entered then the player should be asked to enter again.
    If a 4 streak is reached by a particular player, then the
    game should end. The winner should be declared.

    Parameters
    ----------
    game : class
        It is a basic class consist of initial setup of board and additional functionalities
    choice : int
        Choice of AI agent
    rows: int
     Describe the number of rows of the game board
    columns: int
    Describe the number of coluoumns of the game board
    """
    # 0 is assigned as Player and 1 as AI
    PLAYER = 0
    AI = 1
    # Used to define which turn the game happens
    turn = 0
    # Run until valid depth and type of algorithm are choosen
    while True:
        x = int(input("Enter 1 for minimax and 2 for alpha beta pruning:"))
        depth = int(input("Enter the depth value:"))
        if (x==1 or x==2) and (0 < depth < 100) :
            break
        elif not(0 < depth < 100):
            print("Enter a valid depth value!!")
        else:
            print("Enter a valid number for choosing between minimax and alhpa beta pruning!!")
    # Run until game board is full
    while (not game.is_board_full()):
        # Check for player turn      
        if turn == PLAYER:
                # Take input from the Player to put the piece in certain column
                col = int(input("Player 1 make your selection: "))
                # Call the insert_coin function to insert the coin in the entered column
                game.insert_coin(PLAYER_PIECE,col)
                # Print the player move in the game board
                print("Player move:"+u'\u2193')
                game.print_board()
                # Check if any strak is possible horizontally, vertically, positive diagonally or negative diagonally
                if game.check_for_horizontal_streak(1) or game.check_for_vertical_streak(1) or game.check_for_diagonal_streak_positive(1) or game.check_for_diagonal_streak_negative(1):
                    print("Player 1 wins!!")
                    return None
                # Add 1 and take modulus to alternate between the Player and the AI
                turn += 1
                turn = turn%2

        elif (turn == AI):
            # Copy the board for AI move, because of inheritance I can't do with the class itself
            board = game._board.copy()
            # Check if the choosen algorithm is minimax or alpha_beta_pruning
            if x == 1:
                col, score = minimax(board,depth,True)
            else:
                col, score = alpha_beta_pruning(board,depth,alpha,beta,True)
            # Check if the column move is a valid location
            if game.is_valid_location(col):
                #get the next open row
                row = game.get_next_open_row(col)
                # Drop the piece in the column found after heuristic value evaluation
                game.drop_piece(row, col, AI_PIECE)
                # Print the AI move
                print("AI move:"+u'\u2193')
                game.print_board()
                # Check if any strak is possible horizontally, vertically, positive diagonally or negative diagonally 
                if game.check_for_horizontal_streak(2) or game.check_for_vertical_streak(2) or game.check_for_diagonal_streak_positive(2) or game.check_for_diagonal_streak_negative(2):
                    print("AI wins!!")
                    return None
                turn += 1
                turn = turn%2
    
    return None


def minimax(game,depth,maximizingPlayer):
    """Function to implement minimax algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    game: array
        Game board as a array
    depth: int 
        It is a depth to which AI has to look in
    maximizingPlayer: bool
        Checks for the max or min 
    """
    # Get the valid location we can put piece for the input game array
    valid_locations = get_valid_location(game)
    # Check if the depth is zero or game is over aor board if full
    if depth == 0 or is_board_full(game) or is_game_over(game,AI_PIECE) or is_game_over(game,PLAYER_PIECE):
        # If the board is full or game is over with AI streak or playe streak then return approroiate value
        if is_board_full(game) or is_game_over(game,AI_PIECE) or is_game_over(game,PLAYER_PIECE):
            # Check if the game over with the AI_piece then return high value
            if is_game_over(game,AI_PIECE):
                return (None, 100000000000000)
            # Check if the game over with the minimizing value if so then return large value
            elif is_game_over(game,PLAYER_PIECE):
                return (None, -10000000000000)
            else: 
            # If board is full then return nothing
                return (None, 0)
        else: 
            # If the depth is zero then return the score for the AI_piece
            return (None, score_position(game,AI_PIECE))
    # Check for the AI_piece
    if maximizingPlayer:
        # Initiate the value to the minimum value
        value = -float('inf')
        # Get a random column
        column = random.choice(valid_locations)
        # Iterate through all the valid loations and find the best move
        for col in valid_locations:
            # Extract the open row
            row = get_next_open_row(game, col)
            # Make a copy of the game
            b_copy = game.copy()
            # Drop the piece
            drop_piece(b_copy, row, col, AI_PIECE)
            # Recursively loop until the depth becomes zero
            new_score = minimax(b_copy, depth-1, False)[1]
            # Check if the new_score better than the inital value
            if new_score > value:
                # Assign the best value to the value
                value = new_score
                # Assign the best column to the col
                column = col
        return column, value

    else: 
        value = float('inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(game, col)
            b_copy = game.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value


def alpha_beta_pruning(game,depth,alpha, beta, maximizingPlayer):
    """Function to implement alpha-beta pruning.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    game: array
        It is game represented using array
    depth: int
     Depth unti which AI need to check for
    alpha: float
        Initiate the inital values to + inifinity and - infinity
    maximizingPlayer: bool
        Checks for the max or min 
    """
    valid_locations = get_valid_location(game)
    if depth == 0 or is_board_full(game) or is_game_over(game,AI_PIECE) or is_game_over(game,PLAYER_PIECE):
        if is_board_full(game) or is_game_over(game,AI_PIECE) or is_game_over(game,PLAYER_PIECE):
            if is_game_over(game,AI_PIECE):
                return (None, 100000000000000)
            elif is_game_over(game,PLAYER_PIECE):
                return (None, -10000000000000)
            else: 
                return (None, 0)
        else: 
            return (None, score_position(game,AI_PIECE))

    if maximizingPlayer:
        value = -float('inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(game, col)
            b_copy = game.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = alpha_beta_pruning(b_copy, depth-1,alpha,beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else: 
        value = float('inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(game, col)
            b_copy = game.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = alpha_beta_pruning(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta,value)
            if alpha >= beta:
                break
        return column, value


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--option', choices=[1, 2], type=int)
    parser.add_argument('--board_size', default=[6, 7],  nargs='+', type=int)
    args = parser.parse_args()

    rows = args.board_size[0]
    columns = args.board_size[1]
    opt = args.option

    if opt == 1:
        print("\nMin - Max algorithm\n")
    elif opt == 2:
        print("\nMin - Max algorithm with Alpha-Beta pruning\n")

    game = Connect4(rows, columns)
    # Printing game board
    game.print_board()
    start_time = timeit.default_timer()
    play_game(game,rows,columns)
    end_time = timeit.default_timer()
    time_taken  = end_time - start_time
    print("Time: {}".format(time_taken))

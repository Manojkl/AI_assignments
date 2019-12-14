#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-12-14 13:53:52.203630

@author: Manoj Kolpe Lingappa
"""
import numpy as np
import random

class Connect4:
    """ Class for creating Connect4 game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please fill in the necessary
    functions.
    """

    players = [1, 2]

    def __init__(self, rows, cols):
        """Class Constructor for initializing the board

        Parameters
        ----------
        rows : int 
            Initial position of the board obtained from user
        columns: int
            Initial column soze of the board  
        """
        self.rows =rows
        self.cols = cols
        # Build the game board with numpy array
        self._board = np.asarray([[0 for c in range(cols)] for r in range(rows)])

    def get_valid_location(self):
        """Used to get the valid possible locations from the board

           Return
        ----------
        valid_location: list
         Contains all the possible valid locations
        """
        # Initate the valid location as empty list
        valid_location = []
        # Iterate through all the columns
        for col in range(self.cols):
            # Check if the location is a valid location
            if is_valid_location(self._board,col):
                # If the location found legal then append it to the valid location list
                valid_location.append(col)
        # Return the location
        return valid_location

    
    def check_for_horizontal_streak(self, piece):
        """Class method to check for a horizontal streak given a player,
        board position and a streak value.

        Parameters
        ----------
        piece : int
            check if there is four AI_PIECE or the PLAYER_PIECE horizontally through all rows

        Returns
        -------
        bool:
            Returns True if a horizontal streak is present
        """

        # Iterate until fourth column. That is until where we can make a maximum of 4 continous horizontally
        for j in range(self.cols-3):
        # Iterate through all the rows
            for i in range(self.rows):
                # Check if streak found by going through all the columns (j+1,...) 
                if self._board[i][j] == piece and self._board[i][j+1] == piece and self._board[i][j+2] == piece and self._board[i][j+3] == piece:
                    return True


    def check_for_vertical_streak(self, piece):
        """Class method to check for a vertical streak given a player,
        board position and a streak value.

         Parameters
        ----------
        piece : int
            check if there is four AI_PIECE or the PLAYER_PIECE vertically through all columns

        Returns
        -------
        bool:
            Returns True if vertical streak is present
        """
        # Iterate through all the  columns
        for j in range(self.cols):
        # Iterate through upto only 4th row. That is until where we can make a maximum of 4 continous vertically
            for i in range(self.rows -3):
                # Check if streak found by going through all the rows (i+1,...) 
                if self._board[i][j] == piece and self._board[i+1][j] == piece and self._board[i+2][j] == piece and self._board[i+3][j] == piece:
                    return True

    def check_for_diagonal_streak_positive(self, piece):
        """Class method to check for a diagonal streak given a player,
        board position and a streak value.

        Parameters
        ----------
        piece : int
            check if there is four AI_PIECE or the PLAYER_PIECE diagonally through.

        Returns
        -------
        bool:
            Returns True if positive diagonal streak is present
        """
        # Iterate through columns until self.cols-3
        # [['-' '-' '-' '-' '-' '-' '-']
        # ['-' '-' '-' '-' '-' '-' '-']
        # ['-' '-' '-' '-' '-' '-' '-']
        # ['1' '1' '1' '1' '-' '-' '-']
        # ['1' '1' '1' '1' '-' '-' '-']
        # ['1' '1' '1' '1' '-' '-' '-']]
        for j in range(self.cols-3):
            # Iterate through rows until self.rows -3
            for i in range(self.rows -3):
                # Increment i and j by 1 to go positive diagonally
                if self._board[i][j] == piece and self._board[i+1][j+1] == piece and self._board[i+2][j+2] == piece and self._board[i+3][j+3] == piece:
                    return True


    def check_for_diagonal_streak_negative(self, piece):
        """Class method to check for a diagonal streak given a player,
        board position and a streak value.

        Parameters
        ----------
        piece : int
            check if there is four AI_PIECE or the PLAYER_PIECE diagonally.

        Returns
        -------
        bool:
            Returns True if negative diagonal streak is present
        """
        # Iterate through columns until self.cols-3
        # [['1' '1' '1' '1' '-' '-' '-']
        # ['1' '1' '1' '1' '-' '-' '-']
        # ['1' '1' '1' '1' '-' '-' '-']
        # ['-' '-' '-' '-' '-' '-' '-']
        # ['-' '-' '-' '-' '-' '-' '-']
        # ['-' '-' '-' '-' '-' '-' '-']]
        for j in range(self.cols -3 ):
            # start from 3rd row
            for i in range(3, self.rows):
                # Decrease row and increment the column ((i-1,j+1),.....)
                if self._board[i][j] == piece and self._board[i-1][j+1] == piece and self._board[i-2][j+2] == piece and self._board[i-3][j+3] == piece:
                    return True

    def is_board_full(self):
        """Class method to check if board is full

        Returns
        -------
        bool
            Returns true if board if is full
        """

        for row in self._board:
            for pos in row:
                if pos == 0:
                    return False
        return True

    def insert_coin(self, player, pos):
        """Class method to insert coin in the board

        Parameters
        ----------
        player : string
            Player name whether human or AI agent
        pos : int
            Position to insert on the board

        Returns
        -------
        bool
            Success/Failure of coin
        """

        for row in self._board:
            if row[pos] == 0:
                row[pos] = player
                return True
        print("Position invalid")
        return False

    def print_board(self):
        """Class method to print the board
        Returns
        -------
        None
        """
        board = self._board.copy()
        board  = np.where(board==0, '-', board)
        board  = np.where(board=='1', 'x', board)
        board  = np.where(board=='2', 'o', board)
        print(np.flip(board,0))
        return None

    def is_valid_location(self,col):
        """Class method to check the valid location to insert the piece
        
        Parameters
        ----------
        col : int
            column onto which the validation need to be checked

        Returns
        -------
        bool
        """
        # Check if the top row is empty, i.e it is not occupied by any piece 
        return self._board[self.rows-1][col] == 0

    def get_next_open_row(self, col):
        """Class method toget the next open row
        
        Parameters
        ----------
        col : int
            column onto which the validation need to be checked

        Returns
        -------
        r: row
         which is empty
        """
        # Iterate through all the rows
        for r in range(self.rows):
            # Check if that row contains a 0. It means it is empty
            if self._board[r][col] == 0:
                return r
    
    def drop_piece(self, row, col, piece):
        """Class method to drop the piece
        
        Parameters
        ----------
        col : int
            column onto which the validation need to be checked
        row: int
         row to which i need to insert the piece to
        col: int
         column to which the piece need to be dropped
        Returns
        -------
        board: array
        """

        self._board[row][col] = piece
        return self._board

def evaluate_score(window,piece):
        """Class method to assign score to the current position of the board
        
        Parameters
        ----------
        window: array
            array from which the streaks score need to be found

        piece: int
            AI or player

        Returns
        -------
        score: int
        """
        # Initiate opposite piece as Player
        opp_piece = 1
        # If piece found as Player then make opposite player as AI
        if piece == 1:
            opp_piece = 2
        score = 0
        # Checks if number of piece is equal to 4. If found 4 then increment the score to 100 
        if window.count(piece) == 4:
                score += 100
        # Checks if number of piece is equal to 3 and number of empty lot is 2. If found True then increment the score by 10
        elif (window.count(piece) == 3) and (window.count(0) == 2):
                score += 10
        # Checks if number of piece is equal to 2 and number of empty lot is 2. If found True then increment the score by 5
        elif (window.count(piece) == 2) and (window.count(0) == 2):
                score += 5
        # Checks if number of opposite piece is equal to 3 and number of empty lot is 1. If found True then increment the score by 80
        if window.count(opp_piece) == 3 and window.count(0) == 1:
		        score -= 80
        return score

def score_position(board,piece):
        """Class method to assign score to the current position of the board
        
        Parameters
        ----------
        board: array
            Represent the board as a array

        piece: int
            AI or player

        Returns
        -------
        score: int
        """
        # Extract the number of rows and columns
        board1 = list(board)
        rows =  len(board1)  
        cols =  len(board1[0])
        score = 0
        # Check for centre preference by first getting the centre column and counting the number of AI piece
        centre_array = [int(i) for i in list(board[:,cols//2])]
        centre_count = centre_array.count(piece)
        # Multiply number of counts by 6
        score += centre_count*6
        # Assigning the horizontal score
        # Iterate through all the rows
        for r in range(rows):
            # Extract the all column  for row r
            row_array = [int(i) for i in list(board[r,:])]
            # Iterate through all the columns except last three column since does not make 4 streak
            for c in range(cols -3):
                #Get the window having 4 continous row
                window = row_array[c:c+4]
                # for each combination keep adding the score 
                score += evaluate_score(window,piece)
        
        #Extracting the vertical score
        for c in range(cols):
            # Get all the rows for column c
            col_array = [int(i) for i in list(board[:,c])]
            # Iterate through rows except last 3
            for r in range(rows -3):
                #Get the window having 4 continous column
                window = col_array[r:r+4]
                score += evaluate_score(window,piece)
        
        # positive slope score
        # Iterate through all rows-3
        for r in range(rows-3):
            # Iterate through cols -3 
            for c in range(cols -3):
                # Increment row and column count by 1 each time to get the positive slope
                window = [board[r+i][c+i] for i in range(4)]
                score += evaluate_score(window,piece)
        
        # negative slope score
        # Iterate through all rows-3
        for r in range(rows-3):
            # Iterate through all cols-3
            for c in range(cols -3):
                # Start at the top and keep decremetning the axis 0 and keep incrementing the axis1
                window = [board[r+3-i][c+i] for i in range(4)]
                score += evaluate_score(window,piece)
        return score

def is_valid_location(board,col):
    board = list(board)
    rows =  len(board)
    return board[rows-1][col] == 0

def get_valid_location(board):
    board = list(board)
    cols =  len(board[0])
    valid_location = []
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
    """Class method to get the best move
    
    Parameter
    -------
    board: array
      game board
    piece: int
     AI 
    Returns
    -------
    best_col: int
        Returns the best col for move
    """
    # Get th evalid location
    valid_location = get_valid_location(board)
    best_score = 0
    # Intially make the random colm as the best column
    best_col = random.choice(valid_location)
    # Iterate through all the valid locations
    for col in valid_location:
            # Get the next possible row
            row = get_next_open_row(board,col)
            # make a copy of the board to not to alter the board
            temp_board = board.copy()
            # Drop the piece 
            drop_piece(temp_board,row, col,piece)
            # extract the score
            score = score_position(temp_board,piece)
            # If score found best scor then return the best score and col
            if score > best_score:
                best_score = score
                best_col = col

    return best_col

def is_board_full(board):
    """Class method to check if board is full

    Returns
    -------
    bool
        Returns true if board if is full
    """

    for row in board:
        for pos in row:
            if pos == 0:
                return False
    return True

def insert_coin(board, player, pos):
    """Class method to insert coin in the board

    Parameters
    ----------
    player : string
        Player name whether human or AI agent
    pos : int
        Position to insert on the board

    Returns
    -------
    bool
        Success/Failure of coin
    """

    for row in board:
        if row[pos] == 0:
            row[pos] = player
            return True
    print("Position invalid")
    return False

def is_game_over(board, piece):
    """Class method to check if game is over

    Returns
    -------
    bool
        Return true if the game is over i.e., when human player
        or AI agent has achieved 4 streak
    """
    board = list(board)
    col =  len(board[0])
    row = len(board)
# Check for horizontal streak
    for c in range(col-3):
        for r in range(row):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
# Check for vertical streak
    for c in range(col):
        for r in range(row-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

# Check positively sloped diaganols streak
    for c in range(col-3):
        for r in range(row-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

# Check negatively sloped diaganols streak
    for c in range(col-3):
        for r in range(3, row):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    
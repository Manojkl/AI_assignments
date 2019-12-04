#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-11-16 11:35:50.54

@author: Manoj Kolpe Lingappa (Manojkl)
"""

import copy
import math
from heapq import *
import numpy as np

PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))


class Puzzle:
    """ Class for creating N puzzle game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please try to avoid modifying this
    class unless absolutely necessary.
    """

    def __init__(self, init_state):
        """Class Construction for initializing the board
        NOTE: The 0 tile is the EMPTY tile that can be used
        for swapping.

        Parameters
        ----------
        init_state : list
            Initial position of the board obtained from user
        """

        self.initial_state = init_state
        self.goal_state = [i for i in range(0, PUZZLE_TYPE + 1)]
        self.explored_states = []

    def get_goal_state(self):
        """Class method to get the goal state of the board

        Returns
        -------
        list
            Configuration of board when goal state has been reached
        """
        return self.goal_state

    def get_initial_state(self):
        """Class method to get the initial state of the board

        Returns
        -------
        list
            Initial configuration of board during start of search
        """

        return self.initial_state



def print_puzzle(puzzle):
    """Function to print the puzzle to console

    Parameters
    ----------
    puzzle : list
        8 puzzle configuration
    """

    for idx, val in enumerate(puzzle):

        if (idx + 1) % ROW_SIZE == 0:     
            print("  ", val)
        else:
            print("  ", val, end="")

    return


def move_left(node,position):
    """Function to move one position left in 8 puzzle if possible

    Parameters
    ----------
    node: list
        Initial configuration of tiles before moving left the zero position(swapping)
    position : tuple
        x,y co-ordinate to locate the swapping left position

    Returns
    -------
    list
        Returns the swapped left position and zero position list configuration
    """
    # Convert the list to numpy array
    arr = np.array([node[0:3],
                    node[3:6],
                    node[6:9]])
    #find the value position of the zero
    itemindex = np.where(arr==0)
    # Extract the swapping element postion in the array
    value  = arr[position[1]][position[0]]
    # Make the swapping position as zero
    arr[position[1]][position[0]] = 0   
    # change the zero position as the swapped value 
    arr[int(itemindex[0])][int(itemindex[1])] = value
    # Flattens the numpy array
    arr = arr.ravel()
    # Convert it into a list
    arr = arr.tolist()
    return arr

def move_right(node,position):
    """Function to move one position right in 8 puzzle if possible

    Parameters
    ----------
    node: list
        Initial configuration of tiles before moving right the zero position(swapping)
    position : tuple
        x,y co-ordinate to locate the swapping right position

    Returns
    -------
    list
        Returns the swapped right position and zero position list configuration

    """

    # ind = node.index(0)
    arr = np.array([node[0:3],
                    node[3:6],
                    node[6:9]])
    itemindex = np.where(arr==0)
    value  = arr[position[1]][position[0]]
    arr[position[1]][position[0]] = 0    
    arr[int(itemindex[0])][int(itemindex[1])] = value
    arr = arr.ravel()
    arr = arr.tolist()
    return arr

def move_up(node, position):
    """Function to move one position up in 8 puzzle if possible
    
    node: list
        Initial configuration of tiles before moving up the zero position(swapping)
    position : tuple
        x,y co-ordinate to locate the swapping up position

    Returns
    -------
    list
        Returns the swapped up position and zero position list configurationn]
    """
    arr = np.array([node[0:3],
                    node[3:6],
                    node[6:9]])
    itemindex = np.where(arr==0)
    value  = arr[position[1]][position[0]]
    arr[position[1]][position[0]] = 0    
    arr[int(itemindex[0])][int(itemindex[1])] = value
    arr = arr.ravel()
    arr = arr.tolist()
    return arr

def move_down(node,position):
    """Function to move one position down in 8 puzzle if possible

    node: list
        Initial configuration of tiles before moving down the zero position(swapping)
    position : tuple
        x,y co-ordinate to locate the swapping down position

    Returns
    -------
    list
        Returns the swapped left position and zero down position list configuration
    """
    arr = np.array([node[0:3],
                    node[3:6],
                    node[6:9]])
    itemindex = np.where(arr==0)
    value  = arr[position[1]][position[0]]
    arr[position[1]][position[0]] = 0    
    arr[int(itemindex[0])][int(itemindex[1])] = value
    arr = arr.ravel()
    arr = arr.tolist()
    return arr

def no_of_misplaced_tiles(node):
    """Function to get the number of misplaced tiles for a
    particular configuration

    Parameters
    ----------
    node : list
        List configuration of the node

    Return
    ------
    int
         Returns the number of misplaced tiles
    """
    # Final goal configuration
    goal = [0,1,2,3,4,5,6,7,8]
    # iniitalising
    tiles = 0
    # Iterate through the all the values of the node
    for i in node:
        if i!=0:
            # Calculate the number of mispalced tiles
            if i!=goal[node.index(i)]:
                tiles+=1
    return tiles

def get_manhattan_distance(node):
    """Function to calculate the manhattan distance for a
    particular configuration

    Parameters
    ----------
    node : list
        List configuration of the node

    Return
    ------
    int
        Manhattan distance for the given configuration
    """
    # Convert list to numpy array
    arr = np.array([node[0:3],
                    node[3:6],
                    node[6:9]])
    # Initialising the distace to zero
    distance = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] != 0:
                # Calculate the divmod w.r.t to 3 to get x and y value
                x, y = divmod(arr[i][j], 3)
                # Substract from the i value and add itto the distance
                distance += abs(x - i) + abs(y - j)
    return distance

def saving(puzzle):

    """Function to print the puzzle to console

    Parameters
    ----------
    puzzle : list
        8 puzzle configuration
    """
    master = []
    # Enumerating through each node
    for i in puzzle:    
        list1 = []  
        list2 = []
        # Enumerating through each element
        for idx, val in enumerate(i):
            if (idx+1)%3 != 0:
                # Append the space     
                list2.append(" ")
                # Append the actual value
                list2.append(str(val))
            else:
                list2.append(" ")
                list2.append(str(val))
                m = ''.join(list2)
                list1.append(list(m))
                list2 = []
                
        for i in list1:
                list1[list1.index(i)] = ''.join(i)
        list1.append(" -----")
        master.append(list1)
    return master
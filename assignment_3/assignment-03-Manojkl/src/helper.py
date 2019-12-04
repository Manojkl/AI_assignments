#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday 03 November 2019

@author: Manoj Kolpe Lingappa
"""

import sys
import os
import time
import random
import numpy as np


def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : list
     The list conatain the maze in a list format with each element of list represent the first row of maze grid in string format.

    Returns
    -------
    list
        Extracts start psotion, all the goal position and convert the input maze grid into nested list. Eg. ['abc','de'] = [['a','b','c'],['d','e']] 
    """
    # Initiate the list for make a nested list of all characters of the grid.
    nested_list = []
    # Loop through all the elements of the list
    for i in maze_map:
        # Convert each element which is a string to a list and append to nested_list 
        nested_list.append(list(i))
    # Intiatite list to store all the target position
    target = []
    # Iterate through nested list to find source position.
    for k in nested_list:
        if 's' in k:
            # Once start found put the location of start into tuple.
            index_of_s = (nested_list.index(k),k.index('s'))
    # Initiating indexs to keep track of the position in 2d grid.
    index1 = -1
    index2 = -1
    for i in nested_list:
        index1+=1
        for k in i:
            index2+=1
            # Once the goal found extract the location of the goal and put it into a tuple.
            if k == '*':
                tup = (index1,index2)
                target.append(tup)
        index2 = -1
    return nested_list, index_of_s, target
    
 

def assign_character_for_nodes(maze_map, current_node):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map : list
         The list conatain the maze in a list format with each element of list represent the first row of maze grid in string format.
    current_node : tuple
        Gives the current node positon in (x,y) format

    Returns
    -------
    maze_map : list
         The list conatain the maze in a list format with each element of list represent the first row of maze grid in string format with current node updated to visited 
    """
    # Make the current node as visited by assigning True value to it's position
    maze_map[current_node[0]][current_node[1]] = 'True'

    return maze_map


def write_to_file(path,maze):
    """Function to write output to console and the optimal path
    from start to each goal to txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    path : list of tuples
        It has all the path from starting to the goal.
    maze : list
        The list conatain the maze in a list format with each element of list represent the first row of maze grid in string format.
    """
    # extract the nested_list by calling maze_map_to_tree function
    nested_list, _,_ = maze_map_to_tree(maze)
    # Iterate through nested_list
    for m in nested_list:
        # Remove '\n' from nested list to print nicely in terminal
        try:
            m.remove('\n')
        except ValueError:
            pass
    
    new1 = nested_list
    new = []
    #Iterate through the path
    for track in path:
        # Initiating indexs to keep track of position in the 2d grid
        index1 = -1
        index2 = 0
        # Intiate new_sub to transfer the read maze
        new_sub = []
        # Iterate through the nested_list
        for k in new1:
            index1+=1
            # Iterate through list
            for i in k:
                # Check if the position in the grid is equal to the track position. If True then append the path with '+' else pass read grid from nested_list
                if index1 == track[0] and index2 == track[1]:
                    new_sub.append('+')
                else:
                    new_sub.append(i)
                index2+=1
            # Making it to zero for next row to start from beginning
            index2 = 0
            # Append the new_sub to the new for printing finally.
            new.append(new_sub)
            # Empty it to zero for next row of grid storing.
            new_sub = []
        
        # Merge the nested list for nice printing
        for i in new:
            new[new.index(i)] = ''.join(i)
        # Uncomment this section to view the output in the terminal
        # for k in new:
        #     print(k)
        # We once again convert the joined list into nested list for next operation or plotting next track.
        new2 = []
        for i in new:
            new2.append(list(i))
        # My new maze grid will be new2
        new1 = new2
        # Emptying new for next operation.
        new = []
        # Uncomment this section to slow down the output in terminal
        # time.sleep(0.05)
    # Merging the new2 to print it in a text file
    for i in new2:
            new2[new2.index(i)] = ''.join(i)
    return new2

# To make intial matrix of maze with all obstacles as visited or 'True'
def visiting_matrix(maze):
    # Creating a nested list with same dimension as maze and all initial value as False.
    visited = [['False']*len(maze[0])]*len(maze)
    # Converting the list to numpy array for easy manipulation.
    visited = np.asarray(visited)
    # Initilising the indexes for keeping track of the position
    index1 = -1
    index2 = -1
    # Iterating through maze
    for i in maze:
        index1+=1
        for k in i:
            index2+=1
            # Once the obstacle found make it as True or as visited.
            if k == '=' or k == '|' or k == '\n':
                visited[index1][index2] = 'True'
        index2 = -1
    return visited

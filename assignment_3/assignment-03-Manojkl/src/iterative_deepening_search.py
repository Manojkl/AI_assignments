#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday 03 November 2019

@author: Manoj Kolpe Lingappa
"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes,visiting_matrix

def iterative_deepening_depth_first_search(maze_map, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
     maze_map : list
        The list conatain the maze in a list format with each element of list represent the first row of maze grid in string format.
    start_pos : tuple
        start_pos is the positin of the starting position in (x,y) tuple format.
    goal_pos : tuple
        goal_pos is the position of the goal in tuple format. 

    Returns: list or None
        return the traversing path from start_pos to goal_pos in list format. With first element as start position and last element of list as the goal.
        If goal is not found then it return None.
    """
    # Initialising start to starting position (start_pos)
    start = start_pos
    # Initialising goal to goal position (goal_pos)
    goal = goal_pos
    # converting the input maze list into nested list.
    # Eg. ['abc','de'] = [['a','b','c'],['d','e']]
    list_tree, _, _ = maze_map_to_tree(maze_map)
    # Initialising the queue with initial element as start
    queue = deque([start])
    # Making a nested list same as list_tree such that all non visited position as 'False' and visited position and all obstacles as 'True'
    visited = visiting_matrix(list_tree)
    # Making the starting position as visited
    visited[start_pos[0]][start_pos[1]] = 'True'
    # Initialising the dictionary that store all the keys as parent and values are the children
    dic = {}
    # Intialising while loop to keep checking until the all possible nodes can be explored. 
    while True:
        # Checking whether the queue is empty.
        try:
            # popping elements from queue to explore the children
            popped = queue.popleft()   
        except:
            # If queue is empty and goal is not found then returning with None
            break
        # Popped first element of tuple is the x position in the 2d grid.
        x = popped[0]
        # Popped second element of tuple is the y position in the 2d grid.
        y = popped[1]
        # creating a empty list to store all the children to append to the dictionary with popped as keys and elements in list1 as values
        list1 = []
        # Finding all the neighbour position in 2d grid.
        # N = Up, S = Down, E = Left, W = Right
        N = (x-1,y)
        S = (x+1,y)
        E = (x,y+1)
        W = (x,y-1)
        # Checking if the N[Up] is visited or not by finding value in visited position.and checking whether N[up] position is within the 2d maze grid.
        if visited[W[0]][W[1]] != 'True' and 0 <= W[0] and (len(list_tree)-1)>=W[0] and 0 <= W[1] and (len(list_tree[0])-1)>=W[1]:
            # If the node is not visited then appending the node to the queue.
            queue.append(W)
            # Appending the children of popped parent to append to the dictionary
            list1.append(W)
            # Making the node as visited by passing True value to that position by calling assign_character_for_nodes.
            visited = assign_character_for_nodes(visited,W)
        if visited[E[0]][E[1]] != 'True' and 0 <= E[0] and (len(list_tree)-1)>=E[0] and 0 <= E[1] and (len(list_tree[0])-1)>=E[1]:
            queue.append(E)
            list1.append(E)
            visited = assign_character_for_nodes(visited,E)
        if visited[S[0]][S[1]] != 'True' and 0 <= S[0] and (len(list_tree)-1)>=S[0] and 0 <= S[1] and (len(list_tree[0])-1)>=S[1]:
            queue.append(S)
            list1.append(S)
            visited = assign_character_for_nodes(visited,S)
        if visited[N[0]][N[1]] != 'True' and 0 <= N[0] and (len(list_tree)-1)>=N[0] and 0 <= N[1] and (len(list_tree[0])-1)>=N[1]:
            queue.append(N)
            list1.append(N)
            visited = assign_character_for_nodes(visited,N)    
        dic[popped] = list1
    # Checking whether goal is present in the dictionary keys. If found then go for backtracking if not then return None.
    if goal in dic:
        pass
    else:
        return None
    # Intialising the depth value
    depth = 1
    #  Initialising list path1 for storing all explored nodes
    path1 = []
    # Initialising braking to break out of while loop if goal is reached
    braking = 0
    # Keep checking until goal is reached.
    while True:
        # Checking whwther goal is in the explored path until certain depth.
        for k in path1:
            if k  == goal:
                # changing braking to 1 to break out of while loop
                braking = 1
        # If goal found then break out of while loop or stop exploring.
        if braking == 1:
            break
        # Emptying path1 to store new nodes under new depth limit.
        path1 = []
        # Checking the depth limited search to check whether goal is present under certain certain depth.
        def DLS(start, goal,depth):
            # Checking whether the depth is less than zero while calling recursive function.
            if(depth >=0):
                # Check whether starting position is equal to goal position.
                if(start == goal):
                    # Once the goal found append it to path1 and return the start or just stop exploring.
                    path1.append(start)
                    return start
                # Explore all the children of the parent by extracting children using dictionary.
                values = dic[start]
                # Exploring all the children
                for i in values:
                    # Append all the children to the list to keep track of all explored nodes
                    path1.append(i)
                    # Call recursively until the goal is reached. Now children become the new starting position depth is reduced by 1.
                    DLS(i,goal,depth-1)
            # If depth<0 return None        
            return None
        # call the DLS function
        DLS(start,goal,depth)
        # Increase the depth by 1 at each iteration until the goal is found.
        depth+=1

    # Creating new queue for back propogation.    
    queue1 = deque(path1)
    # Initiate pop1 as goal
    pop1 = goal
    # Intiate new path2 to store all the eploring path.
    path2 = [goal]
    # keep extracting from query until it's empty.
    while queue1:
        # Extracting the second last element of queue to check whether if it is the parent of last element
        pop2 = queue1.pop()
        # Extracting all the children of the pop1 for iteration
        m = dic[pop2]
        # Checking if goal is present in any values of pop2 
        if pop1 in m:
            # If goal is present in any values of pop2 then appending the parent(pop2) as the path
            path2.append(pop2)
             # Now making the pop2 as the new goal by passing it into pop1
            pop1 = pop2
    # All the backtracked path will be in reverse order. Now reversing to go from start to goal.
    path2.reverse()
    print(depth)
    return path2


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    # Finding the position of the starting point and all the target position    
    _, index_of_s, target = maze_map_to_tree(maze_map_map1)
    #  Creating a empty list to append all the explored paths to get printed into text file
    all_maps = []
    # Looping through all the target one by one.
    for i in target:
        # Extracting the path
        path_map1 = iterative_deepening_depth_first_search(maze_map_map1, index_of_s, i)
        # Checking whether there is actually a path exist to the goal
        if path_map1 != None:
            # If goal path is found then extracting the maze with all marked path
            maps = write_to_file(path_map1,maze_map_map1)
            # Appennding all the goal tracking to all_maps for printing it into text file. 
            all_maps.append(maps)
            
    # creating a file for printing the output.
    with open('iddfs_map1.txt', 'w') as f:
        #Iterating through all the paths
            for i in all_maps:
                for item in i:

                    f.write("%s\n" % item)

    _, index_of_s, target = maze_map_to_tree(maze_map_map2)
    all_maps = []
    for i in target:
        path_map2 = iterative_deepening_depth_first_search(maze_map_map2, index_of_s, i)
        if path_map2 != None:
            maps = write_to_file(path_map2,maze_map_map2)
            all_maps.append(maps)
    
    with open('iddfs_map2.txt', 'w') as f:
            for i in all_maps:
                for item in i:
                    f.write("%s\n" % item)

    _, index_of_s, target = maze_map_to_tree(maze_map_map3)
    all_maps = []
    for i in target:
        path_map3 = iterative_deepening_depth_first_search(maze_map_map3, index_of_s, i)
        if path_map3 != None:
            maps = write_to_file(path_map3,maze_map_map3)
            all_maps.append(maps)
    
    with open('iddfs_map3.txt', 'w') as f:
            for i in all_maps:
                for item in i:
                    f.write("%s\n" % item)
    

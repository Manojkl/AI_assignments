#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-11-16 11:35:50.54

@author: Manoj Kolpe Lingappa (Manojkl)
"""

import sys
import timeit
from heapq import *
from helper import *


def Greedy_search(board, opt):
    """Function to implement the Greedy search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : list
        Initial configuration of the game
    opt : int
        If opt = 1 then manhattan distance is used to find the goal configuration. If opt = 2 no of misplaced tiles is used to find the goal configuration 

    Returns
    None
    """
    # Stores the explored nodes
    priority_queue = []
    h_score = 0  # heuristic function value

    # Creating a heap from list to store the nodes with the priority h_score
    heappush(priority_queue, (h_score, board.get_initial_state()))
    # Holds the parent and child node
    list1 = []
    # Used to hold the children of node to append to a dictionary
    list2 = [] 
    # Used to hold the nodes which lead to the goal configuration  
    list3 = [] 
    # Stores all parent as keys and children as values 
    dic = {}   
    # Used to check if goal is reached
    flag = 0
    # Keeps track of the number of nodes visited
    count = 0
    # Holds all the unique nodes to prevent to go into a inifinity loop or visiting same node again.
    set_value = set()
    # Manhattan distance
    if opt == 1:
        # Check until goal is reached
        while flag == 0:
            # Pops out the lowest heuristic value node
            initial_state = heappop(priority_queue)
            # Increment by 1 to update the node visited
            count+=1
            # Extract the zero position in the node
            ind = initial_state[1].index(0)
            # For first row
            if ind <=2:
                ind = (0,ind)
            # Second row
            elif ind >2 and ind<=5:
                ind = (1,ind%3)
            # third row
            else:
                ind = (2,ind%3)
            # x co-ordinate
            x = ind[1]
            # y co-ordinate
            y = ind[0] 
            # Move up co-ordinate
            U = (x,y-1)
            # Move down co-ordinate
            D = (x,y+1)
            # Move left co-ordinate
            L = (x-1,y)
            # Move right co-ordinate
            R = (x+1,y)
            # Checks if the node is visited
            if tuple(initial_state[1]) in set_value:
                is_explored = True
            else:
                is_explored = False
            # Add the visited node to the set
            set_value.add(tuple(initial_state[1]))
            # Checks the co-ordinate is within the boundary of the 3x3 game configuration and nodes not explored
            if U[0] >=0 and U[0] <=2 and U[1] >= 0 and U[1] <=2 and not(is_explored):
                # zero moved up list configuration
                U_list  = move_up(initial_state[1],U)
                # Calculate the heuristic value by calculating manhattan distance
                h_score = get_manhattan_distance(U_list)
                # Push the h_score and U_list to priority queue
                heappush(priority_queue, (h_score,U_list))
                # Append the list configuration and zero move up to the list
                list1.append((tuple(initial_state[1]),tuple(U_list)))
                # children are appended to store in a dictionary with parent as key and children as values
                list2.append(tuple(U_list))
                
            if D[0] >=0 and D[0] <=2 and D[1] >= 0 and D[1] <=2 and not(is_explored):
                # print("entered D")
                D_list  = move_down(initial_state[1],D)
                h_score = get_manhattan_distance(D_list)
                heappush(priority_queue, (h_score, D_list))
                list1.append((tuple(initial_state[1]),tuple(D_list)))
                list2.append(tuple(D_list))
               
            if L[0] >=0 and L[0] <=2 and L[1] >= 0 and L[1] <=2 and not(is_explored):
                # print("entered L")
                L_list  = move_left(initial_state[1],L)
                h_score = get_manhattan_distance(L_list)
                heappush(priority_queue, (h_score, L_list))
                list1.append((tuple(initial_state[1]),tuple(L_list)))
                list2.append(tuple(L_list))
               
            if R[0] >=0 and R[0] <=2 and R[1] >= 0 and R[1] <=2 and not(is_explored):
                # print("entered R")
                R_list  = move_right(initial_state[1],R)
                h_score = get_manhattan_distance(R_list)
                heappush(priority_queue, (h_score, R_list))
                list1.append((tuple(initial_state[1]),tuple(R_list)))
                list2.append(tuple(R_list))
            # Append the parent as key and children as the values
            dic[tuple(initial_state[1])] = list2
            # Empty the list to store the next childrens
            # Check if the goal configuration is reached
            for i in list2:
                if i== tuple(board.get_goal_state()):
                    flag = 1
            list2 = []

        # Take the goal configuration
        goal = tuple(board.get_goal_state())
        # Back tracking until initila configuration is reached.
        while True:
            # Check until the initial configuration is reached
            if goal == tuple(board.get_initial_state()):
                # Append the goal
                list3.append(goal)
                break
            for i in list1:
                # Check if the goal is reached
                if i[1] == goal:
                    list3.append(i[1])
                    # Update the goal as parent of the goal
                    goal = i[0]
                    break
        # Reverse the list to go from initial configuration to the goal configuration
        reverse = list3[::-1]
        # Print all the node configuration 
        for i in reverse:
            print_puzzle(i)
            print("--------")
        string1 = "Nodes explored:"+str(count)
        string2 = "Number of nodes explored to reach goal state:"+str(len(list3)-1)
        print(string1)
        print(string2)
        return reverse, string1, string2
    # This method calls the no_of_misplaced_tiles to calculate the heuristic and find the goal based on the configuration.     
    if opt == 2:        
        while flag == 0:
            count+=1
            initial_state = heappop(priority_queue)
            ind = initial_state[1].index(0)
            if ind <=2:
                ind = (0,ind)
            elif ind >2 and ind<=5:
                ind = (1,ind%3)
            else:
                ind = (2,ind%3)
            x = ind[1]
            y = ind[0] 
            U = (x,y-1)
            D = (x,y+1)
            L = (x-1,y)
            R = (x+1,y)
            
            if tuple(initial_state[1]) in set_value:
                is_explored = True
            else:
                is_explored = False
            set_value.add(tuple(initial_state[1]))
            if U[0] >=0 and U[0] <=2 and U[1] >= 0 and U[1] <=2 and not(is_explored):
                U_list  = move_up(initial_state[1],U)
                # Calculate the heuristic based on the no of misplaced tiles
                h_score = no_of_misplaced_tiles(U_list)
                heappush(priority_queue, (h_score,U_list))
                list1.append((tuple(initial_state[1]),tuple(U_list)))
                list2.append(tuple(U_list))

            if D[0] >=0 and D[0] <=2 and D[1] >= 0 and D[1] <=2 and not(is_explored):
                D_list  = move_down(initial_state[1],D)
                h_score = no_of_misplaced_tiles(D_list)
                heappush(priority_queue, (h_score, D_list))
                list1.append((tuple(initial_state[1]),tuple(D_list)))
                list2.append(tuple(D_list))

            if L[0] >=0 and L[0] <=2 and L[1] >= 0 and L[1] <=2 and not(is_explored):
                L_list  = move_left(initial_state[1],L)
                h_score = no_of_misplaced_tiles(L_list)
                heappush(priority_queue, (h_score, L_list))
                list1.append((tuple(initial_state[1]),tuple(L_list)))
                list2.append(tuple(L_list))

            if R[0] >=0 and R[0] <=2 and R[1] >= 0 and R[1] <=2 and not(is_explored):
                R_list  = move_right(initial_state[1],R)
                h_score = no_of_misplaced_tiles(R_list)
                heappush(priority_queue, (h_score, R_list))
                list1.append((tuple(initial_state[1]),tuple(R_list)))
                list2.append(tuple(R_list))
            dic[tuple(initial_state[1])] = list2

            for i in list2:
                if i == tuple(board.get_goal_state()):
                   flag =1
            list2 = []

        goal = tuple(board.get_goal_state())
        while True:
            if goal == tuple(board.get_initial_state()):
                list3.append(goal)
                break
            for i in list1:
                if i[1] == goal:
                    list3.append(i[1])
                    goal = i[0]
                    break
        reverse = list3[::-1]
        for i in reverse:
            print_puzzle(i)
            print("--------")
        string1 = "Nodes explored:"+str(count)
        string2 = "Number of nodes explored to reach goal state:"+str(len(list3)-1)
        print(string1)
        print(string2)
        return reverse, string1, string2

            
        
if __name__ == '__main__':       
    # puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    # puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing
    # puzzle_8 = [1,0,2,3,4,5,6,7,8]
    print("Initial Configuration")
    board = Puzzle(puzzle_8)
    opt = int(sys.argv[1])
    # print_puzzle(puzzle_8)

    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning Greedy search with Manhattan Dist heuristic\n")
        else:
            print("\nRunning Greedy search with Misplaced Tiles heuristic\n")

        start_time = timeit.default_timer()
        reverse, string1, string2 = Greedy_search(board, opt)
        end_time = timeit.default_timer()
        master = saving(reverse)
        string3 = "Execution time:" +str(end_time - start_time) +" seconds"
        # greedy_Manhattan_Puzzle_1.txt
        # greedy_no_of_misplaced_tiles_Puzzle_1.txt
        with open('greedy_no_of_misplaced_tiles_Puzzle_3.txt', 'w') as f:
            for i in master:
                for item in i:
                    f.write("%s\n" % item)
            # No of nodes explored
            f.write("%s\n" % string1)
            # No of nodes explored to reach the goal state
            f.write("%s\n" % string2)
            #  Time taken for execution
            f.write("%s\n" % string3)
        print('Time: {}s'.format(end_time-start_time))
    else:
        print("Invalid Choice")
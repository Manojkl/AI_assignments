#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes,start_matrix,write_to_file


def iterative_deepening_depth_first_search(maze_map, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [type]
        [description]
    start_pos : [type]
        [description]
    goal_pos : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    start = start_pos
    # print(start)
    goal = goal_pos
    # print(goal)
    list_tree, _ = maze_map_to_tree(maze_map)
    # print(list_tree)
    queue = deque([start])
    # print(queue)
    visited = start_matrix(list_tree)
    visited[start_pos[0]][start_pos[1]] = 'True'
    path = []
    dic = {}
    depth = 0
    testing = 1
    while True:
        for k in path:
            if k == goal:
                print("Found the path")
                # print(path)
                return path
        # print(k)
        queue = deque([start])
        path = []
        depth+=1
        visited = start_matrix(list_tree)
        visited[start_pos[0]][start_pos[1]] = 'True'

        for i in range(depth):
            try:
                popped = queue.popleft()   
            except:
                break
            path.append(popped)
            print("Popped",popped)
            if(popped == goal):
                break
            x = popped[0]
            y = popped[1]
            
            N = (x-1,y)
            S = (x+1,y)
            E = (x,y+1)
            W = (x,y-1)
            print(N,S,E,W)
            if visited[N[0]][N[1]] != 'True' and 0 <= N[0] and (len(list_tree)-1)>=N[0] and 0 <= N[1] and (len(list_tree[0])-1)>=N[1]:
                if i == depth-1:
                    path.append(N)
                else:
                    queue.append(N)
                visited = assign_character_for_nodes(visited,N)
                # print("entered N",visited[N[0]][N[1]])
            if visited[S[0]][S[1]] != 'True' and 0 <= S[0] and (len(list_tree)-1)>=S[0] and 0 <= S[1] and (len(list_tree[0])-1)>=S[1]:
                if i == depth-1:
                    path.append(S)
                else:
                    queue.append(S)
                visited = assign_character_for_nodes(visited,S)
                # print("entered S",visited[1][3])
            if visited[E[0]][E[1]] != 'True' and 0 <= E[0] and (len(list_tree)-1)>=E[0] and 0 <= E[1] and (len(list_tree[0])-1)>=E[1]:
                if i == depth-1:
                    path.append(E)
                else:
                    queue.append(E)
                visited = assign_character_for_nodes(visited,E)
                # print("entered E")
            if visited[W[0]][W[1]] != 'True' and 0 <= W[0] and (len(list_tree)-1)>=W[0] and 0 <= W[1] and (len(list_tree[0])-1)>=W[1]:
                if i == depth-1:
                    path.append(W)
                else:
                    queue.append(W)
                visited = assign_character_for_nodes(visited,W)
            print("Loop is:",i)
            print("path is",path)
            print("Queue is:",queue)    
        
        print("Depth is:",depth)
        print("Path",path)
        while queue:
            pop1 = queue.popleft()   
            path.append(pop1)
            x = pop1[0]
            y = pop1[1]
            if(pop1 == goal):
                break
            N = (x-1,y)
            S = (x+1,y)
            E = (x,y+1)
            W = (x,y-1)
            # print(N,S,E,W)
            if visited[N[0]][N[1]] != 'True' and 0 <= N[0] and (len(list_tree)-1)>=N[0] and 0 <= N[1] and (len(list_tree[0])-1)>=N[1]:
                path.append(N)
                visited = assign_character_for_nodes(visited,N)
            if visited[S[0]][S[1]] != 'True' and 0 <= S[0] and (len(list_tree)-1)>=S[0] and 0 <= S[1] and (len(list_tree[0])-1)>=S[1]:
                path.append(S)
                visited = assign_character_for_nodes(visited,S)
            if visited[E[0]][E[1]] != 'True' and 0 <= E[0] and (len(list_tree)-1)>=E[0] and 0 <= E[1] and (len(list_tree[0])-1)>=E[1]:
                path.append(E)
                visited = assign_character_for_nodes(visited,E)
            if visited[W[0]][W[1]] != 'True' and 0 <= W[0] and (len(list_tree)-1)>=W[0] and 0 <= W[1] and (len(list_tree[0])-1)>=W[1]:
                path.append(W)
                visited = assign_character_for_nodes(visited,W)
        print("Done")       
        if testing == 3:
            print("path is",path)
            return None
        testing+=1
    return path


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

    # CALL THESE FUNCTIONS after filling in the necessary implementations
    start_pos_map1 = (1,3)
    goal_pos_map1 = (16,24)

    path_map1 = iterative_deepening_depth_first_search(maze_map_map1, start_pos_map1, goal_pos_map1)
    # write_to_file("iddfs_map1", path_map1,maze_map_map1)

    # path_map2 = iterative_deepening_depth_first_search(maze_map_map2, start_pos_map2, goal_pos_map2)
    # write_to_file("iddfs_map2", path_map2)

    # path_map3 = iterative_deepening_depth_first_search(maze_map_map3, start_pos_map3, goal_pos_map3)
    # write_to_file("iddfs_map3", path_map3)


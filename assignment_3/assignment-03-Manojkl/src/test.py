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

def fal(visited):
    for i in visited:
        for k in i:
            if k == 'False':
                return 'not'
    return 'yes'

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
    list_tree, _, _ = maze_map_to_tree(maze_map)
    # print(list_tree)
    queue = deque([start])
    # print(queue)
    visited = start_matrix(list_tree)
    visited[start_pos[0]][start_pos[1]] = 'True'
    # print(np.shape(visited))
    nodes = 0
    path = []
    dic = {}
    while True:
        try:
            popped = queue.popleft()   
        except:
            break
        # print(popped)
        path.append(popped)
        nodes+=1
        x = popped[0]
        # print(x)
        y = popped[1]
        list1 = []
        if fal(visited) == 'yes':
            print("found the destination")
            break
        else:
            N = (x-1,y)
            S = (x+1,y)
            E = (x,y+1)
            W = (x,y-1)
            # print(N,S,E,W)
            if visited[W[0]][W[1]] != 'True' and 0 <= W[0] and (len(list_tree)-1)>=W[0] and 0 <= W[1] and (len(list_tree[0])-1)>=W[1]:
                queue.append(W)
                list1.append(W)
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
                # print("entered N",visited[N[0]][N[1]])
            
                # print("entered S",visited[1][3])
            
                # print("entered E")
            
                # print("entered W")
            dic[popped] = list1
    depth = 1
    path1 = []
    print(len(dic))
    braking = 0
    while True:
        
        for k in path1:
            if k  == goal:
                braking = 1
        if braking == 1:
            break
        path1 = []
        def DLS(start, goal,depth):
            if(depth >=0):
                
                if(start == goal):
                    path1.append(start)
                    return start
                values = dic[start]
                for i in values:
                    path1.append(i)
                    DLS(i,goal,depth-1)
                    
            return None
        DLS(start,goal,depth)
        depth+=1
        
    queue1 = deque(path1)
    pop1 = goal
    path2 = [goal]
    while queue1:
        pop2 = queue1.pop()
        m = dic[pop2]
        if pop1 in m:
            path2.append(pop2)
            pop1 = pop2
    path2.reverse()
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

    # CALL THESE FUNCTIONS after filling in the necessary implementations
    start_pos_map2 = (1,3)
    goal_pos_map2 = (18,14)

    # path_map1 = iterative_deepening_depth_first_search(maze_map_map1, start_pos_map1, goal_pos_map1)
    # write_to_file("iddfs_map1", path_map1,maze_map_map1)

    path_map2 = iterative_deepening_depth_first_search(maze_map_map2, start_pos_map2, goal_pos_map2)
    write_to_file("iddfs_map2", path_map2, maze_map_map2)

    # path_map3 = iterative_deepening_depth_first_search(maze_map_map3, start_pos_map3, goal_pos_map3)
    # write_to_file("iddfs_map3", path_map3)


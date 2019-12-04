#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya
"""

import argparse
import random
import timeit
import os

from helper import *



def hill_climb_simple(start_seq, coordinates):
    """ Function to implement simple hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    randomly restarting at every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : [type]
        [description]
    distance_matrix : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    print("yup",len(start_seq))
    distance_matrix = get_distance_matrix(coordinates)
    best_cost = get_distance(distance_matrix,start_seq)
    best_seq = start_seq
    cost1 = []
    seen_states = []
    total = 0
    curr_seq = start_seq
    curr_seq.append(start_seq[0])
    flag = 0
    curr_dist = 0
    restarts_count = 0
    sequence = get_successors(curr_seq)
    best_cost = get_distance(distance_matrix,curr_seq)
    all_seq = []
    for _ in range(5):
        for i in range(2000):   
            for k in sequence:
                if flag != 1:
                    cost = get_distance(distance_matrix,k)
                    if cost<best_cost:
                        best_cost = cost
                        best_seq = k
                        flag = 1
                else:
                    break
            sequence = get_successors(best_seq)
            flag = 0 
            cost1.append(best_cost)

        print("Best cost is",best_cost)
        # print("Best seq", best_seq)
        all_seq.append((best_cost,best_seq))
        copy = start_seq[1:(len(curr_seq)-1)]
        random.shuffle(copy)
        copy.insert(0,curr_seq[0])
        copy.insert(len(copy),curr_seq[-1]) 
        best_seq = copy
        best_cost = get_distance(distance_matrix,copy)
        sequence = get_successors(copy)
        
    plot_cost_function(cost1)
    best_cost, best_seq = min(all_seq, key = lambda t: t[0])
    return best_cost, best_seq


if __name__ == '__main__':

    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    
    # Getting the list of cities and their coordinates
    
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random intial sequence
    random_start_seq = random.sample(range(0, len(list_of_cities[1:])),
                                     len(list_of_cities[1:]))

    # Calculating the least dist using simple hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_simple(random_start_seq,
                                                 coordinates)
    end_time = timeit.default_timer()
    # print(len(best_seq))
    print("Best Sequence:", best_seq)
    print("Least distance from Simple hill climbing:", least_distance)
    print("Time: {}".format(end_time - start_time))

#The Travelling Salesman Problem (TSP) is a classic combinatorial optimisation problem.(combinatorial optimization is a topic that consists of finding an optimal object from a finite set of objects)
#In artificial intelligence, an evolutionary algorithm (EA) is a subset of evolutionary computation,[1] a generic population-based metaheuristic optimization algorithm. An EA uses mechanisms 
#inspired by biological evolution, such as reproduction, mutation, recombination, and selection.
#NP-hard therefore means "at least as hard as any NP-problem.
#Stochastic optimization (SO) methods are optimization methods that generate and use random variables. For stochastic problems, the random variables appear in the formulation of the optimization 
# problem itself, which involves random objective functions or random constraints.
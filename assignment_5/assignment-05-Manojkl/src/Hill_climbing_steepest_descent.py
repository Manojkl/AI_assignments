#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-12-01 09:21:01.885590

@author: Manoj Kolpe Lingappa
"""
import argparse
import os
import random
import timeit

from helper import *


def hill_climb_steepest_descent(start_seq, distance_matrix):
    """ Function to implement steepest descent hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    print the results for every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

   Parameters
    ----------
    start_seq : list
        This has the random starting sequence of the the cities.
    
    coordinates : list 
        This has a coordinate for all the cities in x, y format 

    Returns
    -------
    int (best_cost)
        returns the best cost of the best sequence.
    list (best_seq)
        returns the best sequence with minimum cost.
    """

    # The dictionary has key as two cities and value as distance between between them. Eg. {(x,y):z,....} 
    distance_matrix = get_distance_matrix(coordinates)
    # extracts the best_cost for the starting sequence
    best_cost = get_distance(distance_matrix,start_seq)
    ## Initialising the starting best sequenc as best sequence    
    best_seq = start_seq
    # stores all the cost over 10000 iteration
    all_cost = []
    # setting starting sequence as current sequenc  
    curr_seq = start_seq
    # appending initial element to last of the starting sequence
    curr_seq.append(start_seq[0])
    # stores all the best sequence after every 2000 iteration
    all_seq = []
     # get the sucessor for the current sequence
    sequence = get_successors(curr_seq)
    # get the distance for the curretn sequence
    best_cost = get_distance(distance_matrix,curr_seq)
    # Run for 5 iteration of each having 2000 iteration
    for _ in range(5):
        # Run for 5000 iteration with current sequence
        for i in range(2000):  
            # Iterate through all the sequence generated   
            for k in sequence:
                # get the cost for the current sequence
                cost = get_distance(distance_matrix,k)
                # Check if the cost is better than the best cost
                if cost<best_cost:
                     # If found true then append the current cost to the best cost
                    best_cost = cost
                    # If found true then append the current sequence to the best sequence
                    best_seq = k
            # Append the best cost to the all_cost
            all_cost.append(best_cost)
            # once it out of loop generate a new sequence for the best sequence
            sequence = get_successors(best_seq)

        print("Best cost is",best_cost)
        # Append the best cost and best sequence after every 2000 iteration
        all_seq.append((best_cost,best_seq))
        # slice the current sequence to generate new random sequence
        copy = start_seq[1:(len(curr_seq)-1)]
        # Shuffle the copy
        random.shuffle(copy)
        # insert the starting node back to the list
        copy.insert(0,curr_seq[0])
        # insert the starting node back to the end of list
        copy.insert(len(copy),curr_seq[-1]) 
        # Initiate starting sequence to the as best_seq 
        best_seq = copy
        # Extract the cost for new sequence
        best_cost = get_distance(distance_matrix,copy)
        # extract the successor for the new sequence
        sequence = get_successors(copy)
    # Plot the  graph of cost vs iteration 
    plot_cost_function(all_cost)
    # Find the best cost and best sequenece
    best_cost, best_seq = min(all_seq, key = lambda t: t[0])
    return best_cost, best_seq,all_seq


if __name__ == '__main__':

    # Reading txt file from command line
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

    # Generating a random soln.
    random_seq = random.sample(range(0, len(list_of_cities[1:])),
                               len(list_of_cities[1:]))

    # Calculating the least dist using steepest descent hill climbing
    print(random_seq)
    start_time = timeit.default_timer()
    least_distance, best_seq, all_seq = hill_climb_steepest_descent(random_seq,
                                                           coordinates)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Least distance from Steepest Ascent:", least_distance)
    time_taken = end_time-start_time
    print("Time: {}s".format(time_taken))
    
    if len(random_seq)<60:
        m = "49_cities_steepest_output.txt" 
    else:
        m = "cities_full_steepest_output.txt"
    
    with open(m, 'w') as f:
        #Iterating through all the paths
        key = str("Initial sequence:"+str(random_seq))
        f.write("%s\n" % key)
        for i in all_seq:
                key = "Cost:"+str(i[0])
                f.write("%s\n" % key)
                value = "Sequence:" +str(i[1])
                f.write("%s\n" % value)
        key = "Best cost:"+str(least_distance)
        f.write("%s\n" % key)
        value = "Best sequence:"+str(best_seq)
        f.write("%s\n" % value)
        time_taken = "Time taken by the algorithm:"+ str(time_taken)
        f.write("%s\n" % time_taken)


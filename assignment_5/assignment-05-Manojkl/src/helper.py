#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-12-01 09:21:01.885590

@author: Manoj Kolpe Lingappa
"""
import copy
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def plot_cost_function(cost):
    """ Function to plot the no. of iterations (x-axis) vs
    cost (y-axis). X-axis of the plot should contain xticks
    from 0 to 10000 in steps of 2000.
    Use matplotlib.pyplot to generate the plot as .png file and store it
    in the results folder. An example plot is
    there in the results folder.

    Parameters
    ----------
    cost : list
        This has the corresponding cost for all the 10000 iteration
    """
    # Generatinf all the 10000 values
    t = np.arange(0,10000)
    plt.xlabel("Number of iterations")
    plt.ylabel("Cost")
    plt.plot(t,cost)
    # plt.savefig('/home/manoj/HBRS/AI/Assignments/assignment_5/assignment-05-Manojkl/src/results/plots/Hill_climbing_simple_full_cities.png')
#     plt.savefig('/home/manoj/HBRS/AI/Assignments/assignment_5/assignment-05-Manojkl/src/results/plots/Hill_climbing_steepest_descent_full_cities.png')
    # plt.show()    


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any TWO cities randomly. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city.

    Parameters
    ----------
    curr_seq : list
        This has all the sequence of the possible sequence

    Returns
    -------
    list 
        list has 100 successor sequence        
    """
    # Initialise the empty starting sequence
    seq = []
    # Extract the first and the last sequence 
    temp_seq = curr_seq[1:(len(curr_seq)-1)]
    # Iterate to generate 100 sequence
    for _ in range(100):
            # Generate random l and i for swqpping
            l = random.randint(0, len(temp_seq)-1)
            i = random.randint(0, len(temp_seq)-1)
            # extratc two number such that thery are not equal
            while i==l:
                l = random.randint(0, len(temp_seq)-1)
                i = random.randint(0, len(temp_seq)-1)
            # store in temporary variable
            temp = temp_seq[l]
            temp_seq[l] = temp_seq[i] 
            temp_seq[i] = temp
            # Insert the first value of the sequence to the first and last position of the list
            temp_seq.insert(0,curr_seq[0])
            temp_seq.insert(len(temp_seq),curr_seq[0])
            # append the sequence 
            seq.append(temp_seq)
            temp_seq = curr_seq[1:(len(curr_seq)-1)]
  
    return seq

def get_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : dictionary
        The dictionary has key as two cities and value as distance between between them. Eg. {(x,y):z,....} 
    seq : list
        This has all the sequence

    Returns
    -------
    int
        Finds all the distance between the citites and sum them up
    """
    sum_distance = 0
    number_of_cities = len(seq)
    for i in range(number_of_cities - 1):
        sum_distance+=distance_matrix[seq[i], seq[i+1]]
    
    return sum_distance

def get_distance_matrix(coordinates):
    """ Function to generate a distance matrix. The distance matrix
    is a square matrix.
    For eg: If there are 3 cities then the distance
    matrix has 3 rows and 3 colums, with each city representing a row
    and a column. Each element of the matrix represents the euclidean
    distance between the coordinates of the cities. Thus, the diagonal
    elements will be zero (because it is the distance between the same city).

    Parameters
    ----------
    coordinates : list 
        This has a coordinate for all the cities in x, y format

    Returns
    -------
    dictionary
        The dictionary has key as two cities and value as distance between between them. Eg. {(x,y):z,....}
    """
    dis = {}
    # Enumerate between all the cities one by one and find the distance
    for i, (x1,y1) in enumerate(coordinates):
        for j, (x2,y2) in enumerate(coordinates):
            dx = (float(x2) - float(x1))
            dy = (float(y2) - float(y1))
            distance = math.sqrt(dx*dx + dy*dy)
            dis[i,j] = distance
    return dis  

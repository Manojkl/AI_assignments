#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:49:06 2018

@author: iswariya
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
    ----------```````
    cost : [type]
        [description]
    """
    t = np.arange(0,10000)
    plt.plot(t,cost)
    plt.show()    


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any TWO cities randomly. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city.

    Parameters
    ----------
    curr_seq : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    seq = []
    # m = curr_seq[1:(len(curr_seq)-1)]
    copy1 = curr_seq[1:(len(curr_seq)-1)]
    for _ in range(100):
            l = random.randint(0, len(copy1)-1)
            i = random.randint(0, len(copy1)-1)
            while i==l:
                l = random.randint(0, len(copy1)-1)
                i = random.randint(0, len(copy1)-1)
            temp = copy1[l]
            copy1[l] = copy1[i] 
            copy1[i] = temp
            # copy1 = np.concatenate(([curr_seq[0]],copy1))
            # copy1 = np.append(copy1,curr_seq[0])
            copy1.insert(0,curr_seq[0])
            copy1.insert(len(copy1),curr_seq[0]) 
            seq.append(copy1)
            copy1 = curr_seq[1:(len(curr_seq)-1)]
  
    return seq

def get_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : [type]
        [description]
    seq : [type]
        [description]

    Returns
    -------
    [type]
        [description]
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
    coordinates : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    dis = {}
    for i, (x1,y1) in enumerate(coordinates):
        for j, (x2,y2) in enumerate(coordinates):
            dx = (float(x2) - float(x1))
            dy = (float(y2) - float(y1))
            distance = math.sqrt(dx*dx + dy*dy)
            dis[i,j] = distance
    return dis  
import numpy as np
a = np.array([1,2,3,4,5,6])
c = [11, 44, 33, 40, 18, 34, 17, 26, 45, 5, 8, 41, 21, 16, 31, 47, 14, 22, 19, 28, 3, 7, 24, 12, 15, 30, 35, 27, 46, 23, 4, 29, 9, 43, 36, 38, 39, 20, 48, 0, 10, 13, 6, 37, 25, 32, 42, 1, 2, 11]
least_distance = 9
best_seq = a

all_seq = {123:[12,32,45,67], 45:[98,56,35], 56:[23,11,87]}

with open('output.txt', 'w') as f:
#Iterating through all the paths
    key = str("Initial sequence:"+str(c))
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

b = ((1,2),(3,6),(1,9))

for x,y in enumerate(b):
    print(x,y)
        
import numpy as np
a = np.array([1,2,3,4,5,6])
c = [(3,[1,2,3]),(6,[45,6,8]),(1,[9,2,8,4])]
best_cost, best_seq = min(c, key = lambda t: t[0])
print(best_cost,best_seq)
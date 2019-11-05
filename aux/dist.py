from scipy.stats import wasserstein_distance

import matplotlib.pyplot as plt
import numpy as np

aw = np.arange(1, 11)*2
av = np.arange(0, 10)

bw = np.arange(1, 11)
bv = np.arange(0, 10)

dist = wasserstein_distance(av, bv, aw, bw)
print('The earth movers distance is: {}'.format(dist))

av = np.array([0,3,0,0,0,1,0,0,0,0,0,1,0])
aw = np.array([2,4,6,8,10,12,14,16,18,20,22,24,26])

bv = np.array([0,2,1,0,0,1,0,0,1,0,5,0,0])
bw = np.array([2,4,6,8,10,12,14,16,18,20,22,24,26])

dist = wasserstein_distance(av, bv, aw, bw)
print('The earth movers distance is: {}'.format(dist))

dist = wasserstein_distance([3.4, 3.9, 7.5, 7.8], [4.5, 1.4],
                            [1.4, 0.9, 3.1, 7.2], [3.2, 3.5])
print('The earth movers distance is: {}'.format(dist))

dist = wasserstein_distance([0, 1], [0, 1], [3, 1], [2, 2])
print('The earth movers distance is: {}'.format(dist))

dist = wasserstein_distance([0, 1, 3], [5, 6, 8])
print('The earth movers distance is: {}'.format(dist))

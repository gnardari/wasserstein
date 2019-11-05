from scipy.stats import wasserstein_distance

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

aw = np.arange(1, 11)*2
av = np.arange(0, 10)

bw = np.arange(1, 11)
bv = np.arange(0, 10)

dist = wasserstein_distance(av, bv, aw, bw)
print('The earth movers distance is: {}'.format(dist))

plt.subplot(1,2,1)
sns.distplot(av, hist_kws={'weights': aw},
        bins=len(av), kde=False)

plt.subplot(1,2,2)
sns.distplot(bv, hist_kws={'weights': bw},
        bins=len(bv), kde=False)
plt.show()

av = np.array([0,3,0,0,0,1,0,0,0,0,0,1,0])
aw = np.array([2,4,6,8,10,12,14,16,18,20,22,24,26])

bv = np.array([0,2,1,0,0,1,0,0,1,0,5,0,0])
bw = np.array([2,4,6,8,10,12,14,16,18,20,22,24,26])

plt.subplot(1,2,1)
sns.distplot(av, hist_kws={'weights': aw},
        bins=len(av), kde=False)

plt.subplot(1,2,2)
sns.distplot(bv, hist_kws={'weights': bw},
        bins=len(bv), kde=False)
plt.show()

dist = wasserstein_distance(av, bv, aw, bw)
print('The earth movers distance is: {}'.format(dist))

import numpy as np

w = np.array([1e-8, 0.5, 1.0, 3.7, 1e8])
print(np.max(np.abs(w**-0.5 - 1/np.sqrt(w)) / (1/np.sqrt(w))))

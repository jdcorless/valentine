# Draw a heart in matplotlib
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return 0.8*(np.sqrt(np.abs(x)) + np.sqrt(1-x*x))
def f2(x):
    return 0.8*(np.sqrt(np.abs(x)) - np.sqrt(1-x*x))

x = np.linspace(-1,1,101)
plt.plot(x, f1(x), 'r-')
plt.plot(x, f2(x), 'r-')
plt.xlim(-1.25, 1.25); plt.ylim(-1.0, 1.5)
plt.show()

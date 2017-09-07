import matplotlib.pyplot as plt
import csv
import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('First Graph\n sub-title')
plt.legend()
plt.show()

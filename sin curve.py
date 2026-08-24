import math
import numpy as np 
import matplotlib.pyplot as plt 
y=0
sin_curve = np.linspace(0,5,num=50)
for i in range(1,4):
    y += 5 * np.sin(2*np.pi*10*i*sin_curve)
plt.plot(sin_curve,y)
plt.xlabel('time')
plt.ylabel('sin')
plt.show()
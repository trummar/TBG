# python_fil14.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6, 0.1)

def f1(x): 
    y1 = 2*x+1
    return y1

def f2(x):
    y2 = x**2 - 2
    
    return y2

plt.close('all')
plt.figure(1)
plt.plot(x, f1(x), 'r', label='f1')
plt.plot(x, f2(x), 'g', label='f2') 
#plt.axvline(x = (krysning*3.6), color = "b", label = "Krysning S1 og S2")
plt.legend()
plt.title('Ligninger')
plt.xlabel('x - verdier')
plt.ylabel('y - verdier')
plt.xlim(-10, 10)
plt.ylim(-3, 25)
plt.grid()
plt.show()





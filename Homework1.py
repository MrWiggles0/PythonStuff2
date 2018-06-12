from matplotlib.pyplot import *
from numpy import *
from math import *

t = arange(1,3,0.02)
T = 6*np.log(t)-7*np.exp(0.2*t)

figure(1)
clf()
plot(t,T)

xlabel('Time (min)')
ylabel('Temperature (deg Cel)')
title('Doucette-Plot')

print('Hello World! I just wrote my first Python program. Yayyyyyyyy\nJonathan Doucette')


show()

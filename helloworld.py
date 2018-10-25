import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from __future__ import division
freq=50
time_period=1/freq
time=time_period*2
amplitude=2
t=np.linspace(0,time,500,endpoint=True)
x=2*3.14*freq*t
yc=amplitude*np.sin(x)+1*np.random.rand(len(x))
Fsampling=1000
ts=1/Fsampling
txs=np.arange(0,(time+ts/2),ts)
r=np.round(len(t)/len(txs))

xts=np.arange(0,len(t),r).astype('int')
xs=x[xts]
ys=yc[xts]
fig1=plt.figure(figsize=(10,4))
axes=fig1.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,yc,color='red',linewidth=3,linestyle='-')

plt.show()
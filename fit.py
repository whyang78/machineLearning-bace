import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,20)
y=np.sqrt(x)+0.2*np.random.rand(20)-0.1

def poly_plot(x,y,degree):
    p=np.poly1d(np.polyfit(x,y,degree))
    t=np.linspace(0,1,200)
    plt.plot(x,y,'ro',t,p(t),'-',t,np.sqrt(t),'r--')
    return p

plt.figure(figsize=(18,4))
titles = ['Under Fitting', 'Fitting', 'Over Fitting']
models = [None, None, None]
for index, order in enumerate([1, 3, 10]):
    plt.subplot(1, 3, index + 1)
    models[index] = poly_plot(x, y, order)
    plt.title(titles[index], fontsize=20)

plt.show()
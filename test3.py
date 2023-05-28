# Implementation of matplotlib function 
import matplotlib 
import numpy as np 
import matplotlib.pyplot as plt
import math 
   
np.random.seed(10**7) 
mu = 121 
sigma = 21
x = mu + sigma * np.random.randn(1000) 
   
num_bins = 100
   
n, bins, patches = plt.hist(x, num_bins,  
                            density = 1,  
                            color ='green', 
                            alpha = 0.7) 
   
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2)) 
  
plt.plot(bins, y, '--', color ='black') 
  
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis') 
  
plt.title('matplotlib.pyplot.hist() function Example\n\n', 
          fontweight ="bold") 
  
plt.show()


np.random.seed(10**7) 
n_bins = 20
x = np.random.randn(10000, 3) 
    
colors = ['green', 'blue', 'lime'] 
  
plt.hist(x, n_bins, density = True,  
         histtype ='bar', 
         color = colors, 
         label = colors) 
  
plt.legend(prop ={'size':10}) 
  
plt.title('matplotlib.pyplot.hist() function Example\n\n', 
          fontweight ="bold") 
  
plt.show()

 
def normal_distribution(x, mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
 
 
mean1, sigma1 = 0, 1
x1 = np.linspace(mean1 - 6*sigma1, mean1 + 6*sigma1, 100)
 
mean2, sigma2 = 0, 2
x2 = np.linspace(mean2 - 6*sigma2, mean2 + 6*sigma2, 100)
 
mean3, sigma3 = 5, 1
x3 = np.linspace(mean3 - 6*sigma3, mean3 + 6*sigma3, 100)
 
y1 = normal_distribution(x1, mean1, sigma1)
y2 = normal_distribution(x2, mean2, sigma2)
y3 = normal_distribution(x3, mean3, sigma3)
 
plt.plot(x1, y1, 'r', label='m=0,sig=1')
plt.plot(x2, y2, 'g', label='m=0,sig=2')
plt.plot(x3, y3, 'b', label='m=1,sig=1')
plt.legend()
plt.grid()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import random
x = random.randint(1,100)    
a = np.linspace(-3,5,num=100)
print(len(a))


mean = np.mean(a)
print("Mean : ",mean)
std=np.std(a)
print("Standard Mean : ",std)

def UND (array,mean,std):
    ND_1=1/(np.sqrt(2*np.pi*std**2))
    ND_2=np.exp(-0.5*((array-mean)/std)**2)
    ND= ND_1*ND_2
    return ND
ND = UND(a,mean,std)
plt.plot(a,ND)
plt.title("Univariate Normal Distribution")
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
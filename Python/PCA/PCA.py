import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.randint(10,50,100).reshape(20,5) 
print(x)

#Find Mean
x_mean=np.mean(x,axis=0)
print(x_mean)

#Find Covariance Martix
x_cov=np.cov(x,rowvar=False)
print(x_cov)
np.shape(x_cov)

#Eigen values & Vector
X_evar,X_evec=np.linalg.eigh(x_cov)
print(X_evar,X_evec)


sort_index=np.argsort(X_evar)[::-1]
sort_eval=X_evar[sort_index]
sort_e_vec=X_evec[:,sort_index]
n_componant=2
X_evec_subject=sort_e_vec[:,0:n_componant]

#Transform Data
x_PCA = np.dot(X_evec_subject.transpose(),x_mean.transpose()).transpose()
print(x_PCA)
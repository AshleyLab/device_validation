import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt 
data=np.loadtxt('errors.cleaned.txt',skiprows=1)
labels=[str(i) for i in range(1,61)]
model=TSNE(n_components=2,random_state=0)
data_fitted=model.fit_transform(data)
print str(data_fitted)
fig,ax=plt.subplots()
ax.scatter(data_fitted[:,0],data_fitted[:,1])
for i in range(len(labels)):
    ax.annotate(str(labels[i]),(data_fitted[i,0],data_fitted[i,1]))
plt.show()



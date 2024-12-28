import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

# Load the "gatlin" image data
X = np.loadtxt('gatlin.csv', delimiter=',')
print(X)

# Perform SVD decomposition

U, S, VT = np.linalg.svd(X)

# Plot the original image
plt.figure(1)
plt.imshow(X, cmap=cm.Greys_r)
plt.title('Original image (rank 480)')
plt.axis('off')
plt.draw()

variables = {}  # Dictionnaire pour stocker les variables
k_values = [10, 20, 50, 100, 200]  # Liste des valeurs pour k

for k in k_values:
    variables[k] = np.matmul(np.matmul(U[:, :k], np.diag(S[:k])), VT[:k, :])
    
X10 = variables[10]
X20 = variables[20]
X50 = variables[50]
X100 = variables[100]
X200 = variables[200]


for k in [10, 20, 50, 100, 200] :
    print("L'erreur associée à k =",k,"est",np.linalg.norm(X-variables[k]))


plt.figure(2)   

# Rank 10 approximation
plt.subplot(321)
plt.imshow(X10, cmap=cm.Greys_r)
plt.title('Best rank' + str(10) + ' approximation')
plt.axis('off')

# Rank 20 approximation
plt.subplot(322)
plt.imshow(X20, cmap=cm.Greys_r)
plt.title('Best rank' + str(20) + ' approximation')
plt.axis('off')

# Rank 50 approximation
plt.subplot(323)
plt.imshow(X50, cmap=cm.Greys_r)
plt.title('Best rank' + str(50) + ' approximation')
plt.axis('off')

# Rank 100 approximation
plt.subplot(324)
plt.imshow(X100, cmap=cm.Greys_r)
plt.title('Best rank' + str(100) + ' approximation')
plt.axis('off')

# Rank 200 approximation
plt.subplot(325)
plt.imshow(X200, cmap=cm.Greys_r)
plt.title('Best rank' + str(200) + ' approximation')
plt.axis('off')

# Original
plt.subplot(326)
plt.imshow(X, cmap=cm.Greys_r)
plt.title('Original image (Rank 480)')
plt.axis('off')

plt.draw()

absc = [k for k in range(len(S))]
ord = S

plt.clf()
plt.scatter(absc, ord)
plt.show()

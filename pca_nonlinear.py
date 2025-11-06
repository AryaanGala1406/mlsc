import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.decomposition import KernelPCA
from sklearn.preprocessing import StandardScaler

# Data Loading - Nonlinear dataset (moons)
X, y = make_moons(n_samples=200, noise=0.1, random_state=0)

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Kernel PCA with RBF kernel
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
X_kpca = kpca.fit_transform(X_scaled)

# Plot kernel PCA result
plt.figure(figsize=(8,6))
plt.scatter(X_kpca[:,0], X_kpca[:,1], c=y)
plt.xlabel('Kernel Principal Component 1')
plt.ylabel('Kernel Principal Component 2')
plt.title('Kernel PCA: Nonlinear Data (Moons)')
plt.colorbar()
plt.grid(True)
plt.tight_layout()
plt.show()

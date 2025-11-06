import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Data Loading - Iris is approximately linear
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# Data Preprocessing: Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)  # Reduce to 2 components
principal_components = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)

# Plot the first two principal components
plt.figure(figsize=(8,6))
plt.scatter(principal_components[:,0], principal_components[:,1], c=iris.target)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: Linear Data (Iris)')
plt.colorbar()
plt.grid(True)
plt.tight_layout()
plt.show()

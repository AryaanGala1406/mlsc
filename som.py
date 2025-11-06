from minisom import MiniSom
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Data Loading
iris = datasets.load_iris()
data = iris.data

# Data Preprocessing: Normalize data
data_scaled = MinMaxScaler().fit_transform(data)

# Define SOM parameters and initialize
som = MiniSom(7, 7, data.shape[1], sigma=1.0, learning_rate=0.5, neighborhood_function='triangle', random_seed=0)
som.pca_weights_init(data_scaled)
som.train_random(data_scaled, 100)

# Visualize SOM distance map (U-matrix)
plt.figure(figsize=(7, 7))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar()
plt.show()

# Calculate quantization error as accuracy measure
q_error = som.quantization_error(data_scaled)
print(f'Quantization Error: {q_error}')

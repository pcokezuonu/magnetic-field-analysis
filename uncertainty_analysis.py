import numpy as np

# Example observational magnetic-field measurements
measurements = np.array([120, 125, 130, 128, 122])

# Statistical calculations
mean_value = np.mean(measurements)
std_dev = np.std(measurements)

print("Mean Magnetic Field:", mean_value)
print("Standard Deviation (Uncertainty):", std_dev)

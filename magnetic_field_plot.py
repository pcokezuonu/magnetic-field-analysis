import numpy as np
import matplotlib.pyplot as plt

# Example observational data
Bpos = np.array([50, 80, 120, 200, 350, 500])
SFE = np.array([0.09, 0.07, 0.06, 0.04, 0.025, 0.015])

# Plot
plt.figure(figsize=(7,5))
plt.scatter(Bpos, SFE)

plt.xlabel('Magnetic Field Strength (microG)')
plt.ylabel('Star Formation Efficiency')
plt.title('Magnetic Field Strength vs Star Formation Efficiency')

plt.grid(True)
plt.show()
